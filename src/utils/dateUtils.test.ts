// dateUtil.test.ts

import { describe, it, expect } from 'vitest';
import { extractYearFromChineseDateString } from './dateUtils';

describe('extractYearFromChineseDateString', () => {
  it('should extract the year from a common era date string', () => {
    expect(extractYearFromChineseDateString('2023年')).toBe(2023);
  });

  it('should extract the year from a before common era date string', () => {
    expect(extractYearFromChineseDateString('前2023年')).toBe(-2023);
  });

  it('should return null for an invalid date string', () => {
    expect(extractYearFromChineseDateString('invalid date string')).toBeNull();
  });

  it('should return null for an empty string', () => {
    expect(extractYearFromChineseDateString('')).toBeNull();
  });

  it('should handle single-digit years', () => {
    expect(extractYearFromChineseDateString('前5年')).toBe(-5);
    expect(extractYearFromChineseDateString('5年')).toBe(5);
  });

  it('should handle multi-digit years', () => {
    expect(extractYearFromChineseDateString('123年')).toBe(123);
    expect(extractYearFromChineseDateString('前123年')).toBe(-123);
  });
});
