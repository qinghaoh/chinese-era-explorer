import React, { useState, useEffect, useCallback } from 'react';
import { Select, Group, Box } from '@mantine/core';
import { useForm } from '@mantine/form';
import SearchButton from './SearchButton';
import { Dynasty } from '@/types';

interface EmperorSearchProps {
  onSubmit: (dynasty: string, emperor: string) => void;
}

const EmperorSearchForm: React.FC<EmperorSearchProps> = ({ onSubmit }) => {
  const [dynastiesData, setDynastiesData] = useState<Dynasty[]>([]);
  const [error, setError] = useState<string | null>(null);
  const form = useForm({
    initialValues: {
      dynasty: '',
      emperor: '',
    },
  });

  // Load dynasties data
  useEffect(() => {
    const fetchDynastiesData = async () => {
      try {
        const data = await import('../../data/dynasties.json');
        setDynastiesData(data.default as Dynasty[]);
        setError(null);
      } catch (err: unknown) {
        if (err instanceof Error) {
          setError(`Failed to load dynasties data: ${err.message}`);
        } else {
          setError('Failed to load dynasties data: An unknown error occurred');
        }
      }
    };

    fetchDynastiesData();
  }, []);

  const handleSubmit = (values: typeof form.values) => {
    onSubmit(values.dynasty, values.emperor);
  };

  const getDynastyOptions = useCallback(() => {
    const result = dynastiesData.reduce(
      (acc, dynasty) => {
        const group = acc.find((g) => g.group === dynasty.group);
        const item = { value: String(dynasty.id), label: dynasty.display_name || dynasty.name };
        if (group) {
          group.items.push(item);
        } else {
          acc.push({ group: dynasty.group, items: [item] });
        }
        return acc;
      },
      [] as { group: string; items: { value: string; label: string }[] }[]
    );

    const others = result.filter((g) => g.group === '其他');
    const rest = result.filter((g) => g.group !== '其他');
    return [...rest, ...others];
  }, [dynastiesData]);

  // Dynamic options for the emperor select based on selected dynasty
  const emperorOptions = [
    ...new Map(
      (dynastiesData.find((d) => String(d.id) === form.values.dynasty)?.emperors || [])
        .filter((emperor) => emperor[1] !== '？')
        .map((emperor) => [emperor[1], emperor])
    ).values(),
  ].map((emperor) => ({
    value: String(emperor[0]),
    label: emperor[1],
  }));

  if (error) {
    return <div>Error: {error}</div>; // Displaying the error in the UI
  }

  return (
    <Box maw={400} mx="auto" mt="md">
      <form onSubmit={form.onSubmit(handleSubmit)}>
        <Group justify="center" mt="md" gap="xl" wrap="nowrap">
          <Select
            label="朝代"
            value={form.values.dynasty}
            onChange={(value) => {
              form.setFieldValue('dynasty', value || '');
              form.setFieldValue('emperor', ''); // Reset the emperor value
            }}
            placeholder="全部"
            data={getDynastyOptions()}
            clearable
            searchable
            nothingFoundMessage="無結果..."
            size="md"
          />

          {form.values.dynasty && (
            <Select
              key={form.values.dynasty}
              label="君主"
              value={form.values.emperor}
              onChange={(value) => form.setFieldValue('emperor', value || '')}
              placeholder="全部"
              data={emperorOptions}
              clearable
              searchable
              nothingFoundMessage="無結果..."
              size="md"
            />
          )}
        </Group>

        <Group justify="flex-end" my="md">
          <SearchButton type="submit" disabled={!form.isValid} />
        </Group>
      </form>
    </Box>
  );
};

export default EmperorSearchForm;
