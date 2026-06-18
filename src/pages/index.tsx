import type { ReactNode } from 'react'
import Link from '@docusaurus/Link'
import Layout from '@theme/Layout'
import styles from './index.module.css'

const CATEGORIES = [
  { id: 'visual',     name: '视觉表现',   nameEn: 'Visual Styles',     desc: '从极简到繁复的视觉语言',     count: 10, color: '#1f4e79' },
  { id: 'eastern',    name: '东方古典',   nameEn: 'Eastern Classical', desc: '东方传统美学与现代设计的融合', count: 7,  color: '#c0392b' },
  { id: 'color',      name: '配色方案',   nameEn: 'Color Schemes',     desc: '色彩的情感与象征',           count: 7,  color: '#a855f7' },
  { id: 'typography', name: '字体排版',   nameEn: 'Typography',        desc: '字体的性格与节奏',           count: 6,  color: '#0891b2' },
  { id: 'era',        name: '时代年代',   nameEn: 'Era',               desc: '时代精神在视觉上的回响',     count: 6,  color: '#c89732' },
  { id: 'material',   name: '材质纹理',   nameEn: 'Material',          desc: '触觉延伸到视觉',             count: 6,  color: '#7c2d12' },
  { id: 'modern',     name: '现代趋势',   nameEn: 'Modern Trends',     desc: '当下与未来的设计语言',       count: 10, color: '#059669' },
]

const FEATURED = [
  { slug: 'minimalism',    category: 'visual',  name: '极简主义',  bg: '#ffffff', border: '#000000', text: '#000000' },
  { slug: 'cyberpunk',     category: 'visual',  name: '赛博朋克',  bg: '#0a0a0a', border: '#ff006e', text: '#00f5ff' },
  { slug: 'chinese-ink',   category: 'eastern', name: '中国水墨',  bg: '#f5e8c7', border: '#1a1a1a', text: '#1a1a1a' },
  { slug: 'morandi',       category: 'color',   name: '莫兰迪',    bg: '#d4b5b0', border: '#a8b8c8', text: '#3a3a3a' },
  { slug: 'neon',          category: 'color',   name: '霓虹荧光',  bg: '#0a0a0a', border: '#ff10f0', text: '#39ff14' },
  { slug: 'pixel-retro',   category: 'visual',  name: '像素复古',  bg: '#003049', border: '#fcbf49', text: '#fcbf49' },
  { slug: 'glassmorphism', category: 'visual',  name: '玻璃拟态',  bg: 'linear-gradient(135deg,#7c3aed,#ec4899)', border: 'rgba(255,255,255,0.4)', text: '#ffffff' },
  { slug: 'bauhaus',       category: 'visual',  name: '包豪斯',    bg: '#f5e8c7', border: '#e63946', text: '#1a1a1a' },
  { slug: 'modern-tech',   category: 'modern',  name: '现代科技',  bg: 'linear-gradient(135deg,#0a1628,#1e3a8a)', border: '#3b82f6', text: '#ffffff' },
]

export default function Home(): ReactNode {
  return (
    <Layout
      title="Zero-Style · 设计风格图鉴"
      description="52 种设计风格的系统图鉴,7 大分类,涵盖视觉表现、东方古典、配色方案、字体排版、时代年代、材质纹理、现代趋势">
      <header className={styles.hero}>
        <div className={styles.heroInner}>
          <span className={styles.heroEyebrow}>VISUAL STYLE ATLAS · 设计风格图鉴</span>
          <h1 className={styles.heroTitle}>52 种设计风格</h1>
          <p className={styles.heroSubtitle}>从极简到繁复 · 从古典到未来</p>
          <p className={styles.heroLead}>
            一本面向设计师、开发者、品牌人的视觉风格百科。<br/>
            每种风格包含起源、特征、配色、字体、适用场景与代表案例。
          </p>
          <div className={styles.heroCta}>
            <Link to="/all-styles" className={`${styles.heroBtn} ${styles.heroBtnPrimary}`}>
              浏览全部 52 种 →
            </Link>
            <Link to="/docs/intro" className={`${styles.heroBtn} ${styles.heroBtnSecondary}`}>
              关于项目
            </Link>
          </div>
        </div>
      </header>

      <section className={styles.stats}>
        <div className={styles.statsInner}>
          <div className={styles.statItem}>
            <div className={styles.statNum}>52</div>
            <div className={styles.statLabel}>设计风格</div>
          </div>
          <div className={styles.statItem}>
            <div className={styles.statNum}>7</div>
            <div className={styles.statLabel}>分类体系</div>
          </div>
          <div className={styles.statItem}>
            <div className={styles.statNum}>100+</div>
            <div className={styles.statLabel}>代表案例</div>
          </div>
          <div className={styles.statItem}>
            <div className={styles.statNum}>∞</div>
            <div className={styles.statLabel}>设计灵感</div>
          </div>
        </div>
      </section>

      <section className={styles.categories}>
        <h2 className={styles.sectionTitle}>七大分类</h2>
        <p className={styles.sectionSubtitle}>
          按风格关注点分类 — 从视觉表现到现代趋势,涵盖设计史的脉络
        </p>
        <div className={styles.categoryGrid}>
          {CATEGORIES.map(cat => (
            <Link
              key={cat.id}
              to={`/docs/styles/${cat.id}`}
              className={styles.categoryCard}
              style={{ ['--cat-color' as any]: cat.color }}
            >
              <div className={styles.catHeader}>
                <h3 className={styles.catName}>{cat.name}</h3>
                <span className={styles.catNameEn}>{cat.nameEn}</span>
              </div>
              <p className={styles.catDesc}>{cat.desc}</p>
              <div className={styles.catFooter}>
                <span className={styles.catCount}>{cat.count} 种</span>
                <span className={styles.catArrow}>→</span>
              </div>
            </Link>
          ))}
        </div>
      </section>

      <section className={styles.featured}>
        <h2 className={styles.sectionTitle}>精选风格</h2>
        <p className={styles.sectionSubtitle}>点击卡片查看详情</p>
        <div className={styles.featuredGrid}>
          {FEATURED.map(f => (
            <Link
              key={f.slug}
              to={`/docs/styles/${f.category}/${f.slug}`}
              className={styles.featCard}
              style={{
                background: f.bg,
                border: `2px solid ${f.border}`,
                color: f.text,
              }}
            >
              <span className={styles.featLabel}>{f.name}</span>
            </Link>
          ))}
        </div>
      </section>

      <section className={styles.quote}>
        <div className={styles.quoteInner}>
          <p className={styles.quoteText}>
            "设计不只是它看起来怎样、感觉怎样,<br/>
            设计就是它怎样工作。"
          </p>
          <p className={styles.quoteAttr}>— Steve Jobs</p>
        </div>
      </section>
    </Layout>
  )
}
