import React from 'react';
import { Card, Text, Title, Divider, Group, ThemeIcon } from '@mantine/core';
import { IconCalendar, IconCrown } from '@tabler/icons-react';
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
        <Group justify="Flex-start">
          <ThemeIcon variant="white" size="md" color="blue">
            <IconCalendar style={{ width: '70%', height: '70%' }} />
          </ThemeIcon>
          <Text>
            {era.start} - {era.end}
          </Text>
        </Group>
      )}

      {era.remark && <Text>{era.remark}</Text>}

      {emperor && (
        <Group justify="Flex-start">
          <ThemeIcon variant="white" size="md" color="yellow">
            <IconCrown style={{ width: '70%', height: '70%' }} />
          </ThemeIcon>
          {(emperor.title || emperor.name) && (
            <Text>
              {emperor.title} {emperor.name}
            </Text>
          )}
        </Group>
      )}

      {emperor && emperor.first_regnal_year && emperor.final_regnal_year && (
        <Text>
          在位時間: {emperor.first_regnal_year} - {emperor.final_regnal_year}
        </Text>
      )}
    </Card>
  </div>
);

export default ChineseEraCard;
