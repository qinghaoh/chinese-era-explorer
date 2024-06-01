import React from 'react';
import { Tabs } from '@mantine/core';
import ChineseEraSearchForm from './ChineseEraSearchForm';
import EmperorSearchForm from './EmperorSearchForm';
import DateRangeSearchForm from './DateRangeSearchForm';
import classes from './SearchTabs.module.css';

interface SearchTabsProps {
  onSearchChineseEraName: (era: string) => void;
  onSearchDates: (startYear: number, endYear: number) => void;
  onSearchEmperors: (dynasty: string, emperor: string) => void;
  className?: string;
}

const SearchTabs: React.FC<SearchTabsProps> = ({
  onSearchChineseEraName,
  onSearchDates,
  onSearchEmperors,
}) => {
  const handleEraSubmit = (era: string): void => {
    onSearchChineseEraName(era);
  };

  const handleDateRangeSubmit = (startYear: number, endYear: number): void => {
    onSearchDates(startYear, endYear);
  };

  const handleEmperorSubmit = (dynasty: string, emperor: string) => {
    onSearchEmperors(dynasty, emperor);
  };

  return (
    <Tabs
      variant="unstyled"
      defaultValue="chineseEraName"
      orientation="horizontal"
      classNames={classes}
    >
      <Tabs.List justify="center">
        <Tabs.Tab value="chineseEraName" py="md">
          按年號搜索
        </Tabs.Tab>
        <Tabs.Tab value="dates" py="md">
          按年份範圍搜索
        </Tabs.Tab>
        <Tabs.Tab value="emperors" py="md">
          按朝代/君主搜索
        </Tabs.Tab>
      </Tabs.List>

      <Tabs.Panel value="chineseEraName" py="md">
        <ChineseEraSearchForm onSubmit={handleEraSubmit} />
      </Tabs.Panel>
      <Tabs.Panel value="dates" py="md">
        <DateRangeSearchForm onSubmit={handleDateRangeSubmit} />
      </Tabs.Panel>
      <Tabs.Panel value="emperors" py="md">
        <EmperorSearchForm onSubmit={handleEmperorSubmit} />
      </Tabs.Panel>
    </Tabs>
  );
};

export default SearchTabs;
