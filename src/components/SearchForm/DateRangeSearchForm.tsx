import { useForm } from '@mantine/form';
import { Box, Group, Stack } from '@mantine/core';
import YearInput from '../EraComponents/YearInput';
import SearchButton from './SearchButton';

interface DateRangeSearchFormProps {
  onSubmit: (startYear: number, endYear: number) => void;
}

const DateRangeSearchForm: React.FC<DateRangeSearchFormProps> = ({ onSubmit }) => {
  const form = useForm({
    initialValues: {
      startYear: 0,
      startEra: '公元',
      endYear: 0,
      endEra: '公元',
    },
  });

  const handleSubmit = (values: typeof form.values) => {
    const computeYear = (year: number, era: string) =>
      era === '公元' ? Math.abs(year) : -Math.abs(year);
    onSubmit(
      computeYear(values.startYear, values.startEra),
      computeYear(values.endYear, values.endEra)
    );
  };

  return (
    <Box maw={400} mx="auto">
      <form onSubmit={form.onSubmit(handleSubmit)}>
        <Stack justify="center" gap="md">
          <YearInput form={form} yearField="startYear" eraField="startEra" label="起始年份" />
          <YearInput form={form} yearField="endYear" eraField="endEra" label="終止年份" />
        </Stack>
        <Group justify="flex-end" my="md">
          <SearchButton type="submit" disabled={!form.isValid} />
        </Group>
      </form>
    </Box>
  );
};

export default DateRangeSearchForm;
