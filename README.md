# Zero-Style · 设计风格图鉴

> 一个面向设计师、开发者、品牌人的视觉风格百科。
> **52 种** 设计风格 · **7 大分类** · 部署在 GitHub Pages

## 🌐 在线访问

**https://jeekeagle.github.io/Zero-Style/**

## 📚 收录风格

### 7 大分类

| 分类 | 数量 | 关注点 |
|------|------|--------|
| 视觉表现 | 10 | 从极简到繁复的视觉语言 |
| 东方古典 | 7 | 东方传统美学与现代设计的融合 |
| 配色方案 | 7 | 色彩的情感与象征 |
| 字体排版 | 6 | 字体的性格与节奏 |
| 时代年代 | 6 | 时代精神在视觉上的回响 |
| 材质纹理 | 6 | 触觉延伸到视觉 |
| 现代趋势 | 10 | 当下与未来的设计语言 |

### 完整列表

#### 视觉表现
极简主义 / 孟菲斯 / 新拟物 / 玻璃拟态 / 赛博朋克 / 蒸汽波 / 像素复古 / 瑞士国际 / 包豪斯 / 装饰艺术

#### 东方古典
中国水墨 / 日式禅意 / 浮世绘 / 阿拉伯几何 / 印度曼海蒂 / 唐卷草纹 / 青花瓷

#### 配色方案
莫兰迪 / 马卡龙 / 大地色 / 霓虹 / 单色调 / 复古胶片 / 粉彩

#### 字体排版
衬线经典 / 无衬线现代 / 手写体 / 像素字 / 汉字楷书 / 等宽字

#### 时代年代
Y2K 千禧 / 60年代迷幻 / 80年代复古 / 90年代垃圾 / 70年代迪斯科 / 90年代MTV

#### 材质纹理
纸张纹理 / 毛玻璃 / 金属质感 / 木纹 / 水波纹 / 织物质感

#### 现代趋势
现代科技 / 编辑设计 / 北欧极简 / 暗色优先 / 野兽派 / 杂志风 / 扁平化 / 材料设计 / 3D插画 / 渐变网格

## 🛠️ 技术栈

- [Docusaurus 3](https://docusaurus.io/) — 静态站点生成器
- React + TypeScript
- CSS Modules — 每种风格有专属视觉表征
- GitHub Actions — 自动化部署

## 🏗️ 项目结构

```
Zero-Style/
├── docs/
│   ├── intro.md
│   └── styles/
│       ├── visual/      (10 种风格)
│       ├── eastern/     (7 种风格)
│       ├── color/       (7 种风格)
│       ├── typography/  (6 种风格)
│       ├── era/         (6 种风格)
│       ├── material/    (6 种风格)
│       └── modern/      (10 种风格)
├── src/
│   ├── data/styles.ts         # 风格元数据源
│   ├── css/custom.css         # 全局样式
│   └── pages/
│       ├── index.tsx          # 首页
│       └── all-styles.tsx     # 全部 52 种总览
├── scripts/
│   └── gen_docs.py            # 批量生成器
├── docusaurus.config.ts
├── sidebars.ts
└── .github/workflows/deploy.yml
```

## 🚀 本地开发

```bash
# 安装依赖
npm install

# 启动开发服务器
npm start

# 构建生产版本
npm run build

# 重新生成所有风格文档
npm run gen-docs
```

## ✨ 添加新风格

1. 在 `src/data/styles.ts` 的 `STYLES` 数组中添加新条目
2. 在 `scripts/gen_docs.py` 的对应分类下添加数据(因为 docs 是程序生成的)
3. 运行 `npm run gen-docs` 重新生成 .md 文件
4. 在 `sidebars.ts` 中加入新页面路径
5. 推送到 main,自动触发部署

## 📜 License

MIT
