export interface ChineseEra {
  name: string;
  start: string;
  end: string;
  remark?: string | null;
  emperor_id: number;
}

export interface Emperor {
  id: number;
  dynasty?: string;
  title?: string;
  name: string;
  first_regnal_year?: string;
  final_regnal_year?: string;
}
