import React from 'react';
import { Button } from '@mantine/core';
import { IconSearch } from '@tabler/icons-react';

interface SearchButtonProps {
  type?: 'button' | 'submit' | 'reset';
  disabled?: boolean;
}

function SearchButton({ type = 'button', disabled }: SearchButtonProps) {
  return (
    <Button
      type={type}
      disabled={disabled}
      color="#288c80"
      radius="md"
      leftSection={<IconSearch size={18} />}
      autoContrast
    >
      搜索
    </Button>
  );
}

export default SearchButton;
