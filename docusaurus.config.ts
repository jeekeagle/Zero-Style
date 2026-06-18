import { themes as prismThemes } from 'prism-react-renderer'
import type { Config } from '@docusaurus/types'
import type * as Preset from '@docusaurus/preset-classic'

const config: Config = {
  title: 'Zero-Style · 设计风格图鉴',
  tagline: '52 种设计风格的系统图鉴 · Visual Style Atlas',
  favicon: 'img/favicon.svg',

  url: 'https://jeekeagle.github.io',
  baseUrl: '/Zero-Style/',

  organizationName: 'jeekeagle',
  projectName: 'Zero-Style',

  onBrokenLinks: 'warn',
  onBrokenMarkdownLinks: 'warn',

  i18n: {
    defaultLocale: 'zh-Hans',
    locales: ['zh-Hans'],
  },

  presets: [
    [
      'classic',
      {
        docs: {
          sidebarPath: './sidebars.ts',
          routeBasePath: '/docs',
        },
        blog: false,
        theme: {
          customCss: './src/css/custom.css',
        },
      } satisfies Preset.Options,
    ],
  ],

  themeConfig: {
    image: 'img/social-card.png',
    colorMode: {
      defaultMode: 'light',
      disableSwitch: false,
      respectPrefersColorScheme: true,
    },
    navbar: {
      title: 'Zero-Style',
      logo: { alt: 'Zero-Style', src: 'img/logo.svg' },
      items: [
        { to: '/', label: '首页', position: 'left' },
        { to: '/all-styles', label: '全部 52 种', position: 'left' },
        {
          label: '分类',
          position: 'left',
          items: [
            { label: '视觉表现', to: '/docs/styles/visual' },
            { label: '东方古典', to: '/docs/styles/eastern' },
            { label: '配色方案', to: '/docs/styles/color' },
            { label: '字体排版', to: '/docs/styles/typography' },
            { label: '时代年代', to: '/docs/styles/era' },
            { label: '材质纹理', to: '/docs/styles/material' },
            { label: '现代趋势', to: '/docs/styles/modern' },
          ],
        },
        {
          href: 'https://github.com/jeekeagle/Zero-Style',
          label: 'GitHub',
          position: 'right',
        },
      ],
    },
    footer: {
      style: 'dark',
      links: [
        {
          title: '风格',
          items: [
            { label: '全部 52 种', to: '/all-styles' },
            { label: '视觉表现', to: '/docs/styles/visual' },
            { label: '东方古典', to: '/docs/styles/eastern' },
            { label: '现代趋势', to: '/docs/styles/modern' },
          ],
        },
        {
          title: '相关项目',
          items: [
            { label: 'Zero-Skills', href: 'https://github.com/jeekeagle/Zero-Skills' },
            { label: 'Zero-Skills-Hub', href: 'https://jeekeagle.github.io/Zero-Skills-Hub/' },
          ],
        },
        {
          title: '更多',
          items: [
            { label: 'GitHub 仓库', href: 'https://github.com/jeekeagle/Zero-Style' },
          ],
        },
      ],
      copyright: `© ${new Date().getFullYear()} Zero-Style · 设计风格图鉴`,
    },
    prism: {
      theme: prismThemes.github,
      darkTheme: prismThemes.dracula,
    },
  } satisfies Preset.ThemeConfig,
}

export default config
