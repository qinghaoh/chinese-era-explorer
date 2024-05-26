import { ElementType } from '@/types';

export const elementColors: { [K in ElementType]: string } = {
  金: 'white', // 白
  木: 'cyan', // 青
  水: 'black', // 黑
  火: 'red', // 赤
  土: '#f2ce54', // 黄
};

export const textColorForBackground: { [K in ElementType]: string } = {
  金: 'black', // 黑 on 白
  木: 'darkblue', // 深蓝 on 青
  水: 'white', // 白 on 黑
  火: 'white', // 白 on 赤
  土: 'darkbrown', // 深棕 on 黄
};
