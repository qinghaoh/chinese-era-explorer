import React from 'react';
import { Button, Group, NumberInput } from '@mantine/core';
import { UseFormReturnType } from '@mantine/form';

interface YearInputProps {
  form: UseFormReturnType<any>;
  yearField: string;
  eraField: string;
  label: string;
}

const YearInput: React.FC<YearInputProps> = ({ form, yearField, eraField, label }) => (
  <Group justify="center" mt="md" wrap="nowrap">
    <Button
      variant="light"
      color="#702b3e"
      onClick={() =>
        form.setFieldValue(eraField, form.values[eraField] === '公元' ? '公元前' : '公元')
      }
      mt="lg"
    >
      {form.values[eraField]}
    </Button>
    <NumberInput
      size="md"
      label={label}
      placeholder={`${label} Year`}
      value={form.values[yearField]}
      onChange={(value) => form.setFieldValue(yearField, value)}
      // The year range of Chinese eras is: 公元前140年 - 公元1945年.
      // The input number is the absolute value of a year.
      min={0}
      max={1945}
    />
  </Group>
);

export default YearInput;
