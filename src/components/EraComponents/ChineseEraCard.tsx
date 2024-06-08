import React, { useEffect, useState } from 'react';
import { Card, Text, Title, Group, Box, Avatar } from '@mantine/core';
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

  const [avatarSrc, setAvatarSrc] = useState(null);
  useEffect(() => {
    import(`../../assets/avatars/${emperor.id}.png`)
      .then((module) => setAvatarSrc(module.default))
      .catch(() => setAvatarSrc(null));
  }, [emperor.id]);

  return (
    <Box className={styles['custom-box']}>
      <Card
        shadow="sm"
        radius="md"
        style={{
          height: '100%',
          backgroundImage: `linear-gradient(rgba(255, 255, 255, 0.7), rgba(255, 255, 255, 0.7)),
            url(${oldPaper})`,
          backgroundSize: 'cover',
        }}
      >
        <Card.Section inheritPadding mt="md" style={{ display: 'flex', justifyContent: 'center' }}>
          <Title
            order={1}
            style={{ fontFamily: '標楷體', fontWeight: 'bold', textAlign: 'center' }}
          >
            {era.name}
          </Title>
        </Card.Section>

        {era.start && era.end && (
          <Text size="sm" ta="center" mb="md">
            ({era.start} - {era.end})
          </Text>
        )}

        {era.remark && (
          <Text mt="md" pl="md" pr="md">
            {era.remark}
          </Text>
        )}

        {emperor && (
          <Card.Section
            inheritPadding
            withBorder
            pt="md"
            pb="xl"
            my="md"
            mb="xl"
            style={{
              borderTop: '2px solid black',
              padding: '16px',
            }}
          >
            <Group justify="flex-start" pl="md" pr="md">
              <Avatar src={avatarSrc} alt={`${emperor.name}`} size="lg" />
              {(emperor.title || emperor.name) && (
                <Text size="xl">
                  {emperor.title} {emperor.name}
                </Text>
              )}
            </Group>
            {emperor.first_regnal_year && emperor.final_regnal_year && (
              <Text pl="md" pr="md">
                在位時間: {emperor.first_regnal_year} - {emperor.final_regnal_year}
              </Text>
            )}
          </Card.Section>
        )}
      </Card>
      <Box className={styles['quarter-circle']} style={{ backgroundColor }}>
        <Text className={styles['quarter-circle-text']} style={{ color: textColor }}>
          {emperor.dynasty_name}
        </Text>
      </Box>
    </Box>
  );
};

export default ChineseEraCard;
