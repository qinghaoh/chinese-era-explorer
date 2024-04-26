import React from 'react';
import { Card, Text, Title, Divider } from '@mantine/core';
import { ChineseEra, Emperor } from '../../types';

interface ChineseEraCardProps {
  era: ChineseEra;
  emperor: Emperor;
}

const ChineseEraCard: React.FC<ChineseEraCardProps> = ({ era, emperor }) => (
  <div style={{ margin: '1rem' }}>
    {' '}
    <Card shadow="sm" padding="lg" radius="md" withBorder>
      <Title order={2} style={{ fontFamily: '標楷體', fontWeight: 'bold' }}>
        {era.name}
      </Title>

      <Divider my="sm" />

      {era.start && era.end && (
        <Text>
          {era.start} - {era.end}
        </Text>
      )}
      {era.remark && <Text>{era.remark}</Text>}

      {emperor && (
        <Card shadow="sm" padding="md" style={{ marginTop: '1rem', backgroundColor: '#f8f9fa' }}>
          <Title order={5}>君主</Title>
          {(emperor.title || emperor.name) && (
            <Text>
              {emperor.title} {emperor.name}
            </Text>
          )}
          {emperor.first_regnal_year && emperor.final_regnal_year && (
            <Text>
              在位時間: {emperor.first_regnal_year} - {emperor.final_regnal_year}
            </Text>
          )}
        </Card>
      )}
    </Card>
  </div>
);

export default ChineseEraCard;
