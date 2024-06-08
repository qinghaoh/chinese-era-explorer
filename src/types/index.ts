export type ElementType = '金' | '木' | '水' | '火' | '土';

export interface ChineseEra {
  id: number;
  name: string;
  start: string;
  end: string;
  remark?: string | null;
  emperor_id: number;
  element?: string | null;
}

export interface Emperor {
  id: number;
  dynasty_id: number;
  dynasty_name: string;
  title?: string;
  name: string;
  first_regnal_year?: string;
  final_regnal_year?: string;
}

export interface Dynasty {
  id: number;
  name: string;
  emperors: [number, string][];
  group: string;
  display_name?: string;
}
