import React from 'react';
import { Card, Text, Title, Group, ThemeIcon, Box, Avatar } from '@mantine/core';
import { IconCalendar } from '@tabler/icons-react';
import { ChineseEra, ElementType, Emperor } from '../../types';
import styles from './ChineseEraCard.module.css';
import { elementColors, textColorForBackground } from '@/utils/colorUtils';
import oldPaper from '../../assets/images/grunge-stained-old-paper-texture.jpg';

interface ChineseEraCardProps {
  era: ChineseEra;
  emperor: Emperor;
}

const ChineseEraCard: React.FC<ChineseEraCardProps> = ({ era, emperor }) => {
  const backgroundColor = era.element ? elementColors[era.element as ElementType] : 'transparent';
  const textColor = era.element ? textColorForBackground[era.element as ElementType] : 'black';

  return (
    <Box className={styles['custom-box']}>
      <Card
        shadow="sm"
        padding="lg"
        radius="md"
        style={{
          height: '100%',
          backgroundImage: `linear-gradient(rgba(255, 255, 255, 0.7), rgba(255, 255, 255, 0.7)),
            url(${oldPaper})`,
          backgroundSize: 'cover',
        }}
      >
        <Card.Section
          inheritPadding
          withBorder
          py="sm"
          my="md"
          style={{ display: 'flex', justifyContent: 'center' }}
        >
          <Title
            order={1}
            style={{ fontFamily: '標楷體', fontWeight: 'bold', textAlign: 'center' }}
          >
            {era.name}
          </Title>
        </Card.Section>

        {era.start && era.end && (
          <Group justify="flex-start">
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
          <Card.Section inheritPadding withBorder py="sm" my="md">
            <Group justify="flex-start">
              <Avatar src="avatar.png"></Avatar>
              {(emperor.title || emperor.name) && (
                <Text size="lg">
                  {emperor.title} {emperor.name}
                </Text>
              )}
            </Group>
            {emperor.first_regnal_year && emperor.final_regnal_year && (
              <Text>
                在位時間: {emperor.first_regnal_year} - {emperor.final_regnal_year}
              </Text>
            )}
          </Card.Section>
        )}
      </Card>
      <Box className={styles['quarter-circle']} style={{ backgroundColor }}>
        <Text className={styles['quarter-circle-text']} style={{ color: textColor }}>
          {emperor.dynasty}
        </Text>
      </Box>
    </Box>
  );
};

export default ChineseEraCard;
