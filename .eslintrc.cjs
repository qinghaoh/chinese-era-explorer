module.exports = {
  extends: ['mantine', 'prettier'],
  parserOptions: {
    project: './tsconfig.json',
  },
  rules: {
    'react/react-in-jsx-scope': 'off',
    'import/extensions': 'off',
    'max-len': ['error', { code: 100, comments: 100 }],
  },
};
