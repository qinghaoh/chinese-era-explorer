export function extractYearFromChineseDateString(
  chineseDateStr: string,
): number | null {
  const regex = /^(前)?(\d+)年/
  const match = chineseDateStr.match(regex)

  if (!match) {
    return null
  }

  const isBC = !!match[1]
  const year = parseInt(match[2], 10)

  return isBC ? -year : year
}
