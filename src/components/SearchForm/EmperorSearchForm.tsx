import React, { useState, useEffect } from 'react';
import { Select, Group, Box } from '@mantine/core';
import { useForm } from '@mantine/form';
import SearchButton from './SearchButton';

interface Dynasty {
  name: string;
  emperors: string[];
}

interface EmperorSearchProps {
  onSubmit: (dynasty: string, emperor: string) => void;
}

const EmperorSearchForm: React.FC<EmperorSearchProps> = ({ onSubmit }) => {
  const [dynastiesData, setDynastiesData] = useState<Dynasty[]>([]);
  const form = useForm({
    initialValues: {
      dynasty: '',
      emperor: '',
    },
  });

  // Load dynasties data
  useEffect(() => {
    import('../../data/dynasties.json')
      .then((data) => {
        setDynastiesData(data.default);
      })
      .catch((error) => console.error('Failed to load dynasties data:', error));
  }, []);

  const handleSubmit = (values: typeof form.values) => {
    onSubmit(values.dynasty, values.emperor);
  };

  // Dynamic options for the emperor select based on selected dynasty
  const emperorOptions =
    dynastiesData
      .find((d) => d.name === form.values.dynasty)
      ?.emperors.map((emperor) => ({
        value: emperor,
        label: emperor,
      })) || [];

  return (
    <Box maw={400} mx="auto">
      <form onSubmit={form.onSubmit(handleSubmit)}>
        <Group justify="center" mt="md" gap="xl" wrap="nowrap">
          <Select
            label="朝代"
            value={form.values.dynasty}
            onChange={(value) => form.setFieldValue('dynasty', value || '')}
            placeholder="全部"
            data={dynastiesData.map((dynasty) => ({ value: dynasty.name, label: dynasty.name }))}
            clearable
            searchable
            nothingFoundMessage="無結果..."
          />

          <Select
            label="君主"
            value={form.values.emperor}
            onChange={(value) => form.setFieldValue('emperor', value || '')}
            placeholder="全部"
            data={emperorOptions}
            clearable
            searchable
            nothingFoundMessage="無結果..."
          />
        </Group>

        <Group justify="flex-end" mt="md">
          <SearchButton type="submit" disabled={!form.isValid} />
        </Group>
      </form>
    </Box>
  );
};

export default EmperorSearchForm;
