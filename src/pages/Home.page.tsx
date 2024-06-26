import { Suspense, lazy, useEffect, useState } from 'react';
import { Converter, ConverterOptions, Locale } from 'opencc-js';
import { Container, Grid, Group, Title } from '@mantine/core';
import { ChineseEra, Emperor } from '../types';
import { extractYearFromChineseDateString } from '../utils/dateUtils';

const converterOptions: ConverterOptions = {
  from: 'cn' as Locale,
  to: 't' as Locale,
};

const convertText = Converter(converterOptions);

const SearchTabs = lazy(() => import('../components/SearchForm/SearchTabs'));
const ChineseEraCard = lazy(() => import('../components/EraComponents/ChineseEraCard'));
const Pagination = lazy(() => import('../components/EraComponents/Pagination'));

export function HomePage() {
  // Data loaded from JSON files
  const [erasData, setErasData] = useState<ChineseEra[]>([]);
  const [emperorsData, setEmperorsData] = useState<Emperor[]>([]);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    import('../data/eras.json')
      .then((data) => {
        setErasData(data.default);
      })
      .catch((err) => {
        setError(`Failed to load eras data: ${err.message}`);
      });

    import('../data/emperors.json')
      .then((data) => {
        setEmperorsData(data.default);
      })
      .catch((err) => {
        setError(`Failed to load emperors data: ${err.message}`);
      });
  }, []);

  const [eraResults, setEraResults] = useState<ChineseEra[]>([]);
  const [emperorResults, setEmperorResults] = useState<Emperor[]>([]);
  const [currentPage, setCurrentPage] = useState(1);
  const [itemsPerPage, setItemsPerPage] = useState(10);

  // Each Chinese era has one and only one emperor.
  // Filter emperors by 'id' to match the 'emperor_id' from each era.
  const mapErasToEmperors = (foundEras: ChineseEra[]) => {
    setEraResults(foundEras);

    const foundEmperors = foundEras
      .map((era) => emperorsData.find((emperor) => emperor.id === era.emperor_id))
      .filter((emperor): emperor is Emperor => !!emperor);

    setEmperorResults(foundEmperors);
  };

  // Handlers
  const handleChineseEraNameSearch = (eraInput: string) => {
    // Convert Simplified Chinese to Traditional Chinese
    eraInput = convertText(eraInput);

    const foundEras = erasData.filter((era) => era.name === eraInput);
    mapErasToEmperors(foundEras);
  };

  const handleDatesSearch = (startYear: number, endYear: number) => {
    const foundEras = erasData.filter((era) => {
      const start = extractYearFromChineseDateString(era.start);
      const end = extractYearFromChineseDateString(era.end);
      return start && end && start <= endYear && end >= startYear;
    });
    mapErasToEmperors(foundEras);
  };

  const handleEmperorsSearch = (dynastyInput: string, emperorInput: string) => {
    if (!dynastyInput) {
      mapErasToEmperors(erasData);
      return;
    }

    const processEmperors = (filterCondition: (emperor: Emperor) => boolean) => {
      const foundEmperors = emperorsData.filter(filterCondition);
      // Filter eras by 'emperor_id' to match the 'id' from each emperor.
      const foundEras = foundEmperors
        .map((emp) => erasData.filter((era) => era.emperor_id === emp.id))
        .flat()
        .filter((era): era is ChineseEra => !!era);

      mapErasToEmperors(foundEras);
    };

    if (!emperorInput) {
      // Find all emperors of the dynasty if emperorInput is empty.
      processEmperors((emp) => String(emp.dynasty_id) === dynastyInput);
      return;
    }

    // Find emperors that match the name and, if provided, the title
    processEmperors((emp) => String(emp.id) === emperorInput);
  };

  // Pagination controls
  const lastPageIndex = currentPage * itemsPerPage;
  const firstPageIndex = lastPageIndex - itemsPerPage;
  const currentEraResults = eraResults.slice(firstPageIndex, lastPageIndex);

  // Function to change page
  const paginate = (pageNumber: number) => setCurrentPage(pageNumber);

  if (error) {
    return <div>Error: {error}</div>; // Displaying the error in the UI
  }

  return (
    <>
      <Container size="xl" mt={40}>
        <Group justify="center" mb="lg">
          <Title py="xl" my="xl">
            中國年號查詢
          </Title>
        </Group>

        <Suspense fallback={<div>搜索界面加載中...</div>}>
          <SearchTabs
            onSearchChineseEraName={handleChineseEraNameSearch}
            onSearchDates={handleDatesSearch}
            onSearchEmperors={handleEmperorsSearch}
          />
        </Suspense>

        <Grid gutter={{ base: 5, xs: 'md', md: 'xl', xl: 50 }} my="xl">
          {currentEraResults.map((era, index) => (
            <Grid.Col span={{ base: 12, md: 6, lg: 4 }} key={era.id}>
              {' '}
              <Suspense fallback={<div>搜索結果加載中...</div>}>
                <ChineseEraCard era={era} emperor={emperorResults[firstPageIndex + index]} />
              </Suspense>
            </Grid.Col>
          ))}
        </Grid>

        <Suspense fallback={<div>頁碼加載中...</div>}>
          <Pagination
            itemsPerPage={itemsPerPage}
            totalItems={eraResults.length}
            paginate={paginate}
            currentPage={currentPage}
            setItemsPerPage={setItemsPerPage}
          />
        </Suspense>
      </Container>
    </>
  );
}
