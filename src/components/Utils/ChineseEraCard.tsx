import React from 'react';
import { Card, Text, Group, Title, Divider } from '@mantine/core';
import { ChineseEra, Emperor } from '../../types';

interface ChineseEraCardProps {
  era: ChineseEra;
  emperor: Emperor;
  index: number;
}

const ChineseEraCard: React.FC<ChineseEraCardProps> = ({ era, emperor, index }) => {
  return (
    <div style={{ margin: '1rem' }}>
      {' '}
      <Card shadow="sm" padding="lg">
        <Card.Section>
          <Text>{index + 1}</Text>
        </Card.Section>
        <Divider />
        <Card.Section>
          <Title order={2} style={{ fontFamily: '標楷體', fontWeight: 'bold' }}>
            {era.name}
          </Title>
          {era.start && era.end && (
            <Text>
              起訖時間: {era.start} - {era.end}
            </Text>
          )}
          {era.remark && <Text>備注: {era.remark}</Text>}
        </Card.Section>
        {emperor && (
          <Card shadow="sm" padding="md" style={{ marginTop: '1rem', backgroundColor: '#f8f9fa' }}>
            <Title order={5}>君主</Title>
            <Card.Section>
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
            </Card.Section>
          </Card>
        )}
      </Card>
    </div>
  );
};

export default ChineseEraCard;
