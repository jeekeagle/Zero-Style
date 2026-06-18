import { useState, type ReactNode } from 'react'
import Link from '@docusaurus/Link'
import Layout from '@theme/Layout'
import { CATEGORIES, STYLES } from '../data/styles'
import styles from './all-styles.module.css'

const VISUAL_CLASS_MAP: Record<string, string> = {
  minimal: styles.vMinimal, memphis: styles.vMemphis, neumorph: styles.vNeumorph,
  glass: styles.vGlass, cyber: styles.vCyber, vapor: styles.vVapor,
  pixel: styles.vPixel, swiss: styles.vSwiss, bauhaus: styles.vBauhaus,
  artdeco: styles.vArtDeco, ink: styles.vInk, zen: styles.vZen,
  ukiyo: styles.vUkiyo, arabic: styles.vArabic, mehndi: styles.vMehndi,
  tang: styles.vTang, bluewhite: styles.vBluewhite, morandi: styles.vMorandi,
  macaron: styles.vMacaron, earth: styles.vEarth, neon: styles.vNeon,
  mono: styles.vMono, film: styles.vFilm, pastel: styles.vPastel,
  serif: styles.vSerif, sans: styles.vSans, hand: styles.vHand,
  pixelfont: styles.vPixelfont, kai: styles.vKai, 'mono-font': styles.vMonoFont,
  y2k: styles.vY2K, psychedelic: styles.vPsychedelic, retro80: styles.vRetro80,
  grunge: styles.vGrunge, disco: styles.vDisco, mtv: styles.vMtv,
  paper: styles.vPaper, frost: styles.vFrost, metal: styles.vMetal,
  wood: styles.vWood, water: styles.vWater, fabric: styles.vFabric,
  tech: styles.vTech, editorial: styles.vEditorial, nordic: styles.vNordic,
  dark: styles.vDark, brutal: styles.vBrutal, magazine: styles.vMagazine,
  flat: styles.vFlat, material: styles.vMaterial, '3d': styles.v3d,
  gradient: styles.vGradient,
}

export default function AllStyles(): ReactNode {
  const [activeCat, setActiveCat] = useState<string>('all')

  const filtered = activeCat === 'all'
    ? STYLES
    : STYLES.filter(s => s.category === activeCat)

  return (
    <Layout title="全部 52 种设计风格" description="Zero-Style 全部 52 种设计风格完整列表">
      <div className={styles.page}>
        <header className={styles.header}>
          <h1 className={styles.title}>全部 52 种设计风格</h1>
          <p className={styles.subtitle}>
            点击任意卡片查看风格详情 · 含起源、特征、配色、字体、场景、代表案例
          </p>
          <div className={styles.filterBar}>
            <button
              className={`${styles.filterBtn} ${activeCat === 'all' ? styles.filterBtnActive : ''}`}
              onClick={() => setActiveCat('all')}
            >
              全部 ({STYLES.length})
            </button>
            {CATEGORIES.map(cat => (
              <button
                key={cat.id}
                className={`${styles.filterBtn} ${activeCat === cat.id ? styles.filterBtnActive : ''}`}
                onClick={() => setActiveCat(cat.id)}
              >
                {cat.name} ({STYLES.filter(s => s.category === cat.id).length})
              </button>
            ))}
          </div>
        </header>

        <div className={styles.grid}>
          {filtered.map(s => (
            <Link
              key={s.id}
              to={`/docs/styles/${s.category}/${s.slug}`}
              className={styles.card}
            >
              <div className={`${styles.cardBody} ${VISUAL_CLASS_MAP[s.visual] || styles.vMinimal}`} />
              <div className={styles.cardLabel}>
                <div className={styles.cardName}>{s.nameZh}</div>
                <div className={styles.cardNameEn}>{s.name}</div>
                <p className={styles.cardTagline}>{s.tagline}</p>
              </div>
            </Link>
          ))}
        </div>
      </div>
    </Layout>
  )
}
