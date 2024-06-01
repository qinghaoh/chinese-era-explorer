import React from 'react';
import { Pagination as MantinePagination, Select, Group } from '@mantine/core';

interface PaginationProps {
  itemsPerPage: number;
  totalItems: number;
  paginate: (pageNumber: number) => void;
  currentPage: number;
  setItemsPerPage: (value: number) => void;
}

const Pagination: React.FC<PaginationProps> = ({
  itemsPerPage,
  totalItems,
  paginate,
  currentPage,
  setItemsPerPage,
}) => {
  const totalPages = Math.ceil(totalItems / itemsPerPage);

  return (
    <nav aria-label="Era page navigation">
      <Group align="center" style={{ justifyContent: 'space-between' }}>
        <MantinePagination
          value={currentPage}
          onChange={paginate}
          total={totalPages}
          color="blue"
          withEdges
        />

        <Select
          value={itemsPerPage.toString()}
          onChange={(value) => setItemsPerPage(Number(value))}
          data={[
            { value: '10', label: '10' },
            { value: '20', label: '20' },
            { value: '50', label: '50' },
          ]}
          style={{ width: 100 }}
        />
      </Group>
    </nav>
  );
};

export default React.memo(Pagination);
