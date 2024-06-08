import { Group, TextInput, Box } from '@mantine/core';
import { useForm } from '@mantine/form';
import React from 'react';
import SearchButton from './SearchButton';

interface ChineseEraSearchFormProps {
  onSubmit: (chineseEraName: string) => void; // Simplified onSubmit to only pass the value
}

const ChineseEraSearchForm: React.FC<ChineseEraSearchFormProps> = ({ onSubmit }) => {
  const form = useForm({
    initialValues: {
      chinesesEraName: '',
    },

    validate: {
      chinesesEraName: (value) =>
        /[\u4e00-\u9fff\u3400-\u4DBF]+/g.test(value) || value === '' ? null : '只支持中文字符',
    },
  });

  const handleSubmit = (values: typeof form.values) => {
    onSubmit(values.chinesesEraName);
  };

  return (
    <Box maw={200} mx="auto" my="md">
      <form onSubmit={form.onSubmit(handleSubmit)}>
        <TextInput
          size="md"
          label="年號"
          placeholder="請輸入年號..."
          {...form.getInputProps('chinesesEraName')}
        />
        <Group justify="flex-end" my="md">
          <SearchButton type="submit" disabled={!form.isValid} />
        </Group>
      </form>
    </Box>
  );
};

export default ChineseEraSearchForm;
