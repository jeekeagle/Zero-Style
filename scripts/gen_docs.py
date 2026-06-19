#!/usr/bin/env python3
"""批量生成 52 个风格详情页 + 7 个分类索引页"""
import os
from pathlib import Path

# 与 src/data/styles.ts 完全对应的数据(以可移植方式冗余存储)
STYLES = [
    # ===== 视觉表现 (10) =====
    dict(id='minimalism', slug='minimalism', name='Minimalism', nameZh='极简主义',
         category='visual', year='1960s', tagline='Less is more.',
         description='极简主义起源于 20 世纪中期的视觉艺术运动,以"少即是多"为核心,通过去除一切非必要元素,让形式、内容、空间本身说话。在 UI 设计中表现为大量留白、克制的配色、单一焦点。',
         characteristics=['大量留白', '单一焦点', '克制的配色(单色或双色)', '几何化排版', '去除装饰元素'],
         colors=[('纯白', '#ffffff'), ('纯黑', '#000000'), ('灰', '#f5f5f5')],
         typography='无衬线体(Helvetica, Inter),强调字距与字号对比',
         useCases=['高端品牌官网', '工具类应用', '作品集', '编辑器类 UI'],
         examples=['Apple.com', 'Linear', 'Notion', 'Stripe Press'],
         visual='minimal'),
    dict(id='memphis', slug='memphis', name='Memphis', nameZh='孟菲斯',
         category='visual', year='1981', tagline='打破规则的派对。',
         description='1981 年由意大利设计师 Ettore Sottsass 在米兰创立的孟菲斯设计集团,以鲜艳撞色、几何图形、错位构图挑战现代主义的严肃性。它是后现代主义的视觉宣言。',
         characteristics=['鲜艳撞色(粉、黄、蓝、绿)', '几何图形叠加', '错位与不对称', '图案与条纹', '活泼有趣'],
         colors=[('粉', '#ff6b9d'), ('黄', '#ffd93d'), ('蓝', '#4d96ff'), ('黑', '#000000')],
         typography='粗体无衬线 + 几何形状作装饰',
         useCases=['儿童产品', '潮流品牌', '音乐节', '文创周边'],
         examples=['MTV 早期', 'Vibram', 'Lacoste 联名'],
         visual='memphis'),
    dict(id='neumorphism', slug='neumorphism', name='Neumorphism', nameZh='新拟物',
         category='visual', year='2020', tagline='柔软的浮雕。',
         description='2020 年由设计师 Alexander Plyuto 推广,结合拟物与扁平,使用同色阴影同时表现凸起与凹陷,营造出从背景"长出"的柔软 UI 元素。',
         characteristics=['同色阴影(亮 + 暗)', '凸起与凹陷共存', '低对比度', '背景与元素同色', '极轻的边界'],
         colors=[('米色背景', '#e0e5ec'), ('亮阴影', '#ffffff'), ('暗阴影', '#a3b1c6')],
         typography='常规无衬线,不强调',
         useCases=['仪表盘', '控制中心', '智能家居应用'],
         examples=['Apple Music 概念设计', 'Dribbble 2020 热门'],
         visual='neumorph'),
    dict(id='glassmorphism', slug='glassmorphism', name='Glassmorphism', nameZh='玻璃拟态',
         category='visual', year='2020', tagline='透明与模糊。',
         description='2020 年随 macOS Big Sur 和 Windows 11 流行,以半透明背景 + 背景模糊 + 细边框,模拟磨砂玻璃质感,营造层次感与空间感。',
         characteristics=['半透明背景', '背景模糊(backdrop-filter)', '细边框', '鲜艳背景色', '多层次叠加'],
         colors=[('白半透明', 'rgba(255,255,255,0.2)'), ('紫', '#7c3aed'), ('粉', '#ec4899')],
         typography='现代无衬线,可加阴影增强可读性',
         useCases=['音乐播放器', '钱包类 App', '卡片叠加场景'],
         examples=['Apple Music', 'iOS 控制中心', 'Stripe homepage'],
         visual='glass'),
    dict(id='cyberpunk', slug='cyberpunk', name='Cyberpunk', nameZh='赛博朋克',
         category='visual', year='1980s', tagline='高科技,低生活。',
         description='源自 80 年代科幻文学(William Gibson《神经漫游者》),用霓虹粉/青 + 故障效果 + 暗色背景 + 等宽字体,营造反乌托邦未来感。',
         characteristics=['霓虹色(粉/青/紫)', '故障效果(glitch)', '等宽字体', '暗色背景', '扫描线'],
         colors=[('霓虹粉', '#ff006e'), ('霓虹青', '#00f5ff'), ('黑', '#0a0a0a')],
         typography='等宽字体 + 科技感无衬线',
         useCases=['游戏界面', '音乐人主页', '加密/NFT 网站'],
         examples=['Cyberpunk 2077', 'Blade Runner 2049 海报'],
         visual='cyber'),
    dict(id='vaporwave', slug='vaporwave', name='Vaporwave', nameZh='蒸汽波',
         category='visual', year='2010', tagline='消逝的消费主义。',
         description='2010 年前后在互联网诞生的美学运动,讽刺性怀旧 80/90 年代消费主义,以紫粉渐变、透视网格、希腊雕塑、复古 Windows 截图为核心元素。',
         characteristics=['紫粉渐变', '透视网格', '希腊雕塑', '复古系统 UI', '日文/中文字符'],
         colors=[('紫', '#a855f7'), ('粉', '#ec4899'), ('青', '#06b6d4')],
         typography='粗体未来感字体 + 故障',
         useCases=['音乐厂牌', 'Y2K 复古品牌', '游戏页面'],
         examples=['A E S T H E T I C', 'Macintosh Plus'],
         visual='vapor'),
    dict(id='pixel-retro', slug='pixel-retro', name='Pixel Retro', nameZh='像素复古',
         category='visual', year='1980s', tagline='低分辨率,高表达。',
         description='8-bit/16-bit 时代游戏机的视觉遗产,以像素为单位绘制、限定调色板(8/16/64 色)、黑色硬边描边,塑造出鲜明的怀旧感。',
         characteristics=['像素化图像', '限定调色板(NES 56色等)', '黑色硬边', '等宽像素字体', '方块构图'],
         colors=[('NES 红', '#d62828'), ('NES 蓝', '#003049'), ('NES 黄', '#fcbf49')],
         typography='像素字体(Press Start 2P)',
         useCases=['独立游戏', '复古主题应用', '像素艺术'],
         examples=['Celeste', 'Stardew Valley', 'Shovel Knight'],
         visual='pixel'),
    dict(id='swiss-design', slug='swiss-design', name='Swiss Design', nameZh='瑞士国际',
         category='visual', year='1950s', tagline='理性的网格。',
         description='1950 年代瑞士发展出的平面设计风格,严格基于网格、Helvetica 字体的理性主义设计,强调客观性、可读性与功能性。',
         characteristics=['严格网格', 'Helvetica/Akzidenz-Grotesk', '不对称布局', '黑白主色 + 一红', '照片裁切'],
         colors=[('黑', '#000000'), ('白', '#ffffff'), ('瑞士红', '#e30613')],
         typography='Helvetica / Akzidenz-Grotesk,严谨字号比例',
         useCases=['企业品牌', '公共信息设计', '博物馆导视'],
         examples=['瑞士航空', 'Helvetica 纪录片', 'Müller-Brockmann 海报'],
         visual='swiss'),
    dict(id='bauhaus', slug='bauhaus', name='Bauhaus', nameZh='包豪斯',
         category='visual', year='1919', tagline='形式追随功能。',
         description='1919 年由 Walter Gropius 在德国创立的包豪斯学校,强调艺术与技术的统一,使用基本几何形状(圆/方/三角)和原色,深刻影响现代设计。',
         characteristics=['基本几何形', '三原色(红/蓝/黄)', '无衬线字体', '不对称构图', '功能性至上'],
         colors=[('红', '#e63946'), ('蓝', '#1d3557'), ('黄', '#f1c40f')],
         typography='几何无衬线(Futura,Bauhaus 93)',
         useCases=['品牌识别', '教育产品', '文化机构'],
         examples=['Bauhaus 档案馆', 'Pinterest 包豪斯风'],
         visual='bauhaus'),
    dict(id='art-deco', slug='art-deco', name='Art Deco', nameZh='装饰艺术',
         category='visual', year='1920s', tagline='奢华的几何。',
         description='1920-30 年代法国兴起的装饰艺术风格,以奢华、对称、几何图案(扇形/锯齿/太阳放射)为标志,代表爵士时代的优雅。',
         characteristics=['对称构图', '几何图案(扇形/锯齿)', '奢华金属感', '粗体衬线', '阶梯式'],
         colors=[('金', '#d4af37'), ('深绿', '#0f3a2e'), ('黑', '#1a1a1a')],
         typography='几何衬线(Poiret One,Limelight)',
         useCases=['高端品牌', '酒店', '奢侈品包装'],
         examples=['克莱斯勒大厦', '盖茨比电影'],
         visual='artdeco'),

    # ===== 东方古典 (7) =====
    dict(id='chinese-ink', slug='chinese-ink', name='Chinese Ink Wash', nameZh='中国水墨',
         category='eastern', year='唐宋', tagline='墨分五色。',
         description='起源于唐宋的中国水墨画,以墨色浓淡(焦/浓/重/淡/清)表现山水意境,"留白"为构图核心,讲究气韵生动。',
         characteristics=['浓淡墨色', '大量留白', '山水花鸟主题', '印章与题款', '气韵生动'],
         colors=[('宣纸白', '#f5e8c7'), ('焦墨', '#1a1a1a'), ('朱砂', '#c0392b')],
         typography='毛笔楷书/行书',
         useCases=['文化品牌', '茶/酒包装', '高端文创'],
         examples=['黄公望 富春山居图', '故宫文创'],
         visual='ink'),
    dict(id='japanese-zen', slug='japanese-zen', name='Japanese Zen', nameZh='日式禅意',
         category='eastern', year='14世纪', tagline='侘寂 wabi-sabi。',
         description='日本禅宗美学,以"侘寂"(wabi-sabi)为核心理念,接受不完美、无常、不对称,体现极简、自然、安静的东方哲学。',
         characteristics=['极度留白', '不对称(不对称美)', '自然材质', '单一红点/印章', '静谧氛围'],
         colors=[('米白', '#f5f0e8'), ('墨', '#2c2c2c'), ('朱', '#c43e3e')],
         typography='明朝体(细衬线)',
         useCases=['茶道/花道', '日本料理', '高端极简品牌'],
         examples=['MUJI', '无印良品', '京都旅馆'],
         visual='zen'),
    dict(id='ukiyo-e', slug='ukiyo-e', name='Ukiyo-e', nameZh='浮世绘',
         category='eastern', year='江户', tagline='浮世的瞬间。',
         description='江户时代(17-19 世纪)日本木刻版画,以鲜艳色彩、明确轮廓、平涂色块描绘歌舞伎、艺伎、风景,是日本最具国际影响力的艺术形式。',
         characteristics=['平涂色块', '明确轮廓', '鲜艳对比', '风景/人物', '装饰性边框'],
         colors=[('群青', '#1f3a93'), ('朱', '#c0392b'), ('金', '#d4af37')],
         typography='竖排毛笔字',
         useCases=['艺术海报', '和风产品', '文创周边'],
         examples=['葛饰北斋 神奈川冲浪里', '歌川广员'],
         visual='ukiyo'),
    dict(id='arabic-geometric', slug='arabic-geometric', name='Arabic Geometric', nameZh='阿拉伯几何',
         category='eastern', year='中世纪', tagline='无限的几何。',
         description='伊斯兰艺术因避免偶像崇拜,发展出举世无双的几何图案(Star Pattern)与阿拉伯书法,体现了数学之美与对无限的崇敬。',
         characteristics=['八角星/十二角星', '几何镶嵌', '无始无终', '对称图案', '阿拉伯书法'],
         colors=[('蓝', '#1e3a8a'), ('金', '#d4af37'), ('白', '#ffffff')],
         typography='阿拉伯书法体(Kufi,Naskh)',
         useCases=['清真寺装饰', '中东品牌', '纺织品'],
         examples=['Alhambra 宫', '迪拜世博'],
         visual='arabic'),
    dict(id='indian-mehndi', slug='indian-mehndi', name='Indian Mehndi', nameZh='印度曼海蒂',
         category='eastern', year='古代', tagline='手绘的祝福。',
         description='印度传统身体彩绘艺术,以指甲花(海娜)绘制精细的藤蔓、花卉、几何图案,用于婚礼、宗教节日,象征好运与祝福。',
         characteristics=['精细藤蔓图案', '花卉/几何', '手绘温度', '对称美感', '红褐色'],
         colors=[('海娜棕', '#8b4513'), ('朱砂', '#c0392b'), ('金', '#d4af37')],
         typography='天城文(Devanagari)',
         useCases=['婚礼请柬', '印度节庆', '手工艺品牌'],
         examples=['印度婚礼手绘', 'Diwali 海报'],
         visual='mehndi'),
    dict(id='tang-pattern', slug='tang-pattern', name='Tang Pattern', nameZh='唐卷草纹',
         category='eastern', year='唐代', tagline='连绵的生机。',
         description='唐代盛行的卷草纹(亦称唐草),以 S 形连续曲线串联花朵叶片,源自希腊传入并中国化,象征生生不息。',
         characteristics=['S 形连续曲线', '花卉叶片串联', '对称循环', '金色线条', '繁复精致'],
         colors=[('金', '#d4af37'), ('朱', '#a82d2d'), ('墨', '#1a1a1a')],
         typography='楷书',
         useCases=['国潮品牌', '文创产品', '中式包装'],
         examples=['敦煌壁画', '唐代铜镜'],
         visual='tang'),
    dict(id='blue-white-porcelain', slug='blue-white-porcelain', name='Blue-White Porcelain', nameZh='青花瓷',
         category='eastern', year='元代', tagline='青白之间。',
         description='元代成熟的青花瓷,以钴蓝在白胎上绘画,经高温烧制形成白底蓝花的经典样式,后经丝绸之路远播欧洲,影响深远。',
         characteristics=['白底蓝花', '钴蓝单色', '花卉山水主题', '釉下彩', '对称构图'],
         colors=[('钴蓝', '#1e3a8a'), ('白胎', '#f5f5f0'), ('米色', '#e8e0d0')],
         typography='楷书',
         useCases=['中式餐具', '国风产品', '博物馆文创'],
         examples=['元青花鬼谷下山罐', '景德镇瓷器'],
         visual='bluewhite'),

    # ===== 配色方案 (7) =====
    dict(id='morandi', slug='morandi', name='Morandi', nameZh='莫兰迪',
         category='color', year='现代', tagline='灰调的温柔。',
         description='源自意大利画家 Giorgio Morandi 的静物画色调,以低饱和度的灰调色彩(灰粉/灰蓝/灰绿)营造温柔、宁静、有距离感的氛围。',
         characteristics=['低饱和度', '灰色调', '相近色系', '温柔安静', '高级感'],
         colors=[('灰粉', '#d4b5b0'), ('灰蓝', '#a8b8c8'), ('灰绿', '#b5c4b1')],
         typography='衬线/无衬线均可,克制',
         useCases=['女装品牌', '美妆护肤', '家居设计'],
         examples=['COS', 'MUJI', 'Jellybook'],
         visual='morandi'),
    dict(id='macaron', slug='macaron', name='Macaron', nameZh='马卡龙',
         category='color', year='现代', tagline='甜品的色谱。',
         description='源于法国马卡龙甜品的高明度低饱和色彩,以柔和的粉、薄荷绿、薰衣草紫等组合,营造甜美、少女、清新的视觉氛围。',
         characteristics=['高明度', '低饱和度', '粉嫩色系', '甜美可爱', '轻柔感'],
         colors=[('樱花粉', '#ffd1dc'), ('薄荷', '#b5e5cf'), ('薰衣草', '#e0b8e0')],
         typography='圆润无衬线或手写',
         useCases=['甜品/烘焙', '少女品牌', '母婴产品'],
         examples=['Laduree', 'Pinterest 马卡龙配色'],
         visual='macaron'),
    dict(id='earth-tone', slug='earth-tone', name='Earth Tone', nameZh='大地色',
         category='color', year='原始', tagline='泥土的颜色。',
         description='源自自然大地色彩(棕、米、陶土、橄榄绿),传达温暖、可靠、自然、原始的感受,是户外/家居/手作品牌的常用配色。',
         characteristics=['自然色系', '温暖', '可靠', '原始感', '大地'],
         colors=[('焦糖棕', '#a67c52'), ('陶土', '#c87856'), ('橄榄', '#7a8450'), ('米色', '#e8dcc0')],
         typography='衬线/手写皆宜',
         useCases=['户外品牌', '家居', '手工艺', '咖啡品牌'],
         examples=['Patagonia', 'Glossier', 'Aesop'],
         visual='earth'),
    dict(id='neon', slug='neon', name='Neon', nameZh='霓虹荧光',
         category='color', year='1980s', tagline='电光的色彩。',
         description='高饱和度的荧光色(电光粉/霓虹绿/电子紫),在暗色背景上发光,源自 80 年代夜店与赛博朋克美学,极富活力与未来感。',
         characteristics=['高饱和', '荧光', '暗底发光', '活力', '未来'],
         colors=[('电光粉', '#ff10f0'), ('霓虹绿', '#39ff14'), ('电子紫', '#bc13fe')],
         typography='科技/未来感字体',
         useCases=['游戏', '音乐节', '潮流品牌'],
         examples=['Cyberpunk 2077', 'Tron'],
         visual='neon'),
    dict(id='monochrome', slug='monochrome', name='Monochrome', nameZh='单色调',
         category='color', year='古典', tagline='一色的深度。',
         description='使用同一色相的不同明度/饱和度构成画面,通过层次而非色彩对比制造视觉张力,营造统一、高级、专业的氛围。',
         characteristics=['单一色相', '明度层次', '高级感', '统一性强', '克制'],
         colors=[('蓝深', '#0a1628'), ('蓝中', '#1e3a8a'), ('蓝浅', '#bfdbfe')],
         typography='任一字体,简洁为佳',
         useCases=['企业品牌', '金融', '数据可视化'],
         examples=['IBM', 'Vogue 杂志专题'],
         visual='mono'),
    dict(id='film-retro', slug='film-retro', name='Film Retro', nameZh='复古胶片',
         category='color', year='1970s', tagline='胶片的颗粒。',
         description='模仿 70 年代柯达/富士胶片的色调,以暖黄/橙红阴影、颗粒感、暗角为标志,营造怀旧、温柔、有故事感的氛围。',
         characteristics=['暖色调', '颗粒感', '暗角', '轻微过曝', '复古滤镜'],
         colors=[('暖橙', '#e89b6c'), ('胶片黄', '#f4e4c1'), ('复古蓝', '#5b8fa8')],
         typography='手写/衬线',
         useCases=['生活方式品牌', '人像摄影', '咖啡店'],
         examples=['VSCO 复古滤镜', 'Instagram 胶片风'],
         visual='film'),
    dict(id='pastel', slug='pastel', name='Pastel', nameZh='粉彩',
         category='color', year='1950s', tagline='柔色的梦境。',
         description='粉彩色调源自 50 年代美式家居,以高明度、低饱和度的柔和色彩(粉、薄荷、淡蓝)为主,营造轻盈、温柔、怀旧的氛围。',
         characteristics=['高明度', '低饱和', '柔和', '轻盈', '怀旧'],
         colors=[('粉', '#ffb3ba'), ('薄荷', '#bae1ff'), ('淡黄', '#ffffba'), ('淡紫', '#e0bbff')],
         typography='圆润手写',
         useCases=['婚礼', '婴儿用品', '少女品牌'],
         examples=['美国 50 年代 diner', 'Bando 周边'],
         visual='pastel'),

    # ===== 字体排版 (6) =====
    dict(id='serif-classic', slug='serif-classic', name='Serif Classic', nameZh='衬线经典',
         category='typography', year='15世纪', tagline='笔尖的优雅。',
         description='衬线体(Serif)在字母笔画末端有装饰性衬线,源自 15 世纪古腾堡印刷,代表传统、权威、可读性,常见于书籍、报刊、高端品牌。',
         characteristics=['衬线装饰', '传统感', '高可读性', '权威性', '多用于长文'],
         colors=[('黑', '#1a1a1a'), ('米白', '#f5f0e8')],
         typography='Times New Roman / Garamond / Playfair Display',
         useCases=['书籍', '报刊', '法律文件', '高端品牌'],
         examples=['Vogue', 'The New York Times', 'Hermès'],
         visual='serif'),
    dict(id='sans-modern', slug='sans-modern', name='Sans Modern', nameZh='无衬线现代',
         category='typography', year='20世纪', tagline='干净的呼吸。',
         description='无衬线体(Sans-Serif)去除笔画末端的装饰,以几何或人文风格的简洁造型为标志,代表现代、清晰、中性,广泛应用在屏幕 UI。',
         characteristics=['无衬线', '几何/人文', '屏幕友好', '现代感', '中性'],
         colors=[('任意', '#000000')],
         typography='Helvetica / Inter / SF Pro / Roboto',
         useCases=['科技产品', 'UI 设计', '现代品牌'],
         examples=['Apple', 'Google', 'Spotify'],
         visual='sans'),
    dict(id='hand-written', slug='hand-written', name='Hand Written', nameZh='手写体',
         category='typography', year='永恒', tagline='手的温度。',
         description='手写体强调"人手"的痕迹,从优雅的铜版手写体(Copperplate)到随意的马克笔手写,传达个性、温度、亲密感。',
         characteristics=['手绘痕迹', '个性化', '温度感', '不规则', '亲密'],
         colors=[('墨', '#1a1a1a'), ('暖白', '#f5e8c7')],
         typography='Caveat / Pacifico / Sacramento / 中文手写',
         useCases=['婚礼请柬', '个人品牌', '小品牌'],
         examples=['Instagram 故事', 'Pinterest 手账'],
         visual='hand'),
    dict(id='pixel-font', slug='pixel-font', name='Pixel Font', nameZh='像素字',
         category='typography', year='1980s', tagline='点阵的拼图。',
         description='像素字体由方格像素拼出字母,源自 8-bit 时代游戏机,在低分辨率下保持可读,代表复古、游戏、极客文化。',
         characteristics=['像素方格', '有限像素', '复古游戏', '黑色硬边', '等宽'],
         colors=[('绿', '#39ff14'), ('黑', '#000000')],
         typography='Press Start 2P / VT323 / Pixelify Sans',
         useCases=['复古游戏', '极客文化', '8-bit 设计'],
         examples=['Celeste', 'Shovel Knight', 'Discord 复古主题'],
         visual='pixelfont'),
    dict(id='chinese-kai', slug='chinese-kai', name='Chinese Kai', nameZh='汉字楷书',
         category='typography', year='汉魏', tagline='方正之美。',
         description='楷书起源于汉魏,以端正工整、笔画清晰为特点,是中文印刷与书法的基础字体,代表庄重、文化、可读性。',
         characteristics=['端正工整', '笔画清晰', '印刷友好', '庄重感', '传统美'],
         colors=[('墨', '#1a1a1a'), ('宣纸', '#f5e8c7')],
         typography='楷体 / 思源宋体 / 霞鹜文楷',
         useCases=['书籍', '公告', '文化品牌', '中文 UI'],
         examples=['中文报纸', '方正字库'],
         visual='kai'),
    dict(id='monospace', slug='monospace', name='Monospace', nameZh='等宽字',
         category='typography', year='1960s', tagline='代码的节奏。',
         description='等宽字体(Monospace)每个字符宽度相同,源自打字机时代,在代码编辑、终端、数据表格中保持对齐,代表技术、精确。',
         characteristics=['等宽字符', '技术感', '对齐友好', '终端友好', '极客'],
         colors=[('黑', '#1a1a1a'), ('背景', '#f5f5f5')],
         typography='JetBrains Mono / Fira Code / Menlo / Consolas',
         useCases=['代码编辑器', '终端', '技术博客'],
         examples=['GitHub', 'VS Code', 'iTerm2'],
         visual='mono-font'),

    # ===== 时代年代 (6) =====
    dict(id='y2k', slug='y2k', name='Y2K', nameZh='Y2K 千禧',
         category='era', year='1990s-2000s', tagline='千年虫的乐观。',
         description='Y2K(Year 2000)是 90 年代末-00 年代初的设计风格,以铬金属感、透明塑料、泡泡字、鲜艳渐变体现千禧年的乐观未来主义。',
         characteristics=['铬金属感', '透明塑料', '泡泡字', '蓝紫渐变', '未来乐观'],
         colors=[('铬银', '#c0c0c0'), ('宝蓝', '#0066ff'), ('紫', '#8a2be2'), ('粉', '#ff69b4')],
         typography='Juice Box / Blambot Custom',
         useCases=['潮流品牌', '音乐 MV', '复古文化'],
         examples=['iMac G3', 'Britney Spears MV', 'Spice Girls'],
         visual='y2k'),
    dict(id='psychedelic-60s', slug='psychedelic-60s', name='Psychedelic 60s', nameZh='60年代迷幻',
         category='era', year='1960s', tagline='迷幻的迷醉。',
         description='1960 年代嬉皮士文化与 LSD 影响下的视觉风格,以漩涡图案、霓虹色、扭曲字体、自由反叛为标志。',
         characteristics=['漩涡图案', '霓虹撞色', '扭曲字体', '自由反叛', '迷幻'],
         colors=[('橙', '#ff6600'), ('紫', '#9933ff'), ('黄', '#ffff00')],
         typography='扭曲变形的衬线/无衬线',
         useCases=['音乐节', '复古海报', '嬉皮文化'],
         examples=['Woodstock 海报', 'Yellow Submarine'],
         visual='psychedelic'),
    dict(id='retro-80s', slug='retro-80s', name='Retro 80s', nameZh='80年代复古',
         category='era', year='1980s', tagline='霓虹与磁带。',
         description='1980 年代是 MTV、合成器、Walkman 的时代,设计以霓虹渐变、网格透视、磁带/录像带元素、合成波字体为标志。',
         characteristics=['霓虹渐变', '网格透视', '合成波字体', '磁带元素', '电子感'],
         colors=[('霓虹粉', '#ff10f0'), ('紫蓝', '#6633ff'), ('青', '#00ffff')],
         typography='未来粗体无衬线',
         useCases=['音乐节', '游戏', '复古派对'],
         examples=['Stranger Things 片头', 'Drive 电影海报'],
         visual='retro80'),
    dict(id='grunge-90s', slug='grunge-90s', name='Grunge 90s', nameZh='90年代垃圾摇滚',
         category='era', year='1990s', tagline='破败的反叛。',
         description='90 年代垃圾摇滚(Grunge)与 X 世代反主流文化下的设计,以撕裂纸张、粗糙纹理、不规则排版、DIY 美学为标志。',
         characteristics=['撕裂纸张', '粗糙纹理', '不规则排版', 'DIY 感', '反主流'],
         colors=[('灰', '#6b7280'), ('暗红', '#8b0000'), ('黑', '#1a1a1a')],
         typography='粗黑无衬线,歪斜',
         useCases=['乐队海报', '潮牌', 'Zine 杂志'],
         examples=['Nirvana Nevermind 封面', 'Kurt Cobain T-shirt'],
         visual='grunge'),
    dict(id='disco-70s', slug='disco-70s', name='Disco 70s', nameZh='70年代迪斯科',
         category='era', year='1970s', tagline='舞池的反射。',
         description='1970 年代迪斯科文化的视觉呈现,以镜面球、霓虹条、棕橙暖色、曲线字体为代表,传递享乐、派对、自由的氛围。',
         characteristics=['镜面球', '霓虹条', '棕橙暖色', '曲线字体', '享乐主义'],
         colors=[('焦糖', '#c87856'), ('金', '#d4af37'), ('棕', '#5c3317')],
         typography='曲线感的衬线',
         useCases=['派对海报', '复古音乐', '酒店品牌'],
         examples=['Saturday Night Fever 海报', 'Studio 54'],
         visual='disco'),
    dict(id='mtv-90s', slug='mtv-90s', name='MTV 90s', nameZh='90年代MTV',
         category='era', year='1990s', tagline='频道的视觉。',
         description='1990 年代 MTV 音乐频道的美学,以手绘涂鸦、撞色、碎片拼贴、卡通字体为代表,是 X 世代青年文化的视觉代表。',
         characteristics=['手绘涂鸦', '撞色', '碎片拼贴', '卡通字体', '青年文化'],
         colors=[('柠檬黄', '#ffff00'), ('天蓝', '#00bfff'), ('品红', '#ff1493')],
         typography='粗体卡通字体',
         useCases=['音乐节', '复古品牌', '潮牌'],
         examples=['MTV 早期片头', 'Beavis & Butthead'],
         visual='mtv'),

    # ===== 材质纹理 (6) =====
    dict(id='paper-texture', slug='paper-texture', name='Paper Texture', nameZh='纸张纹理',
         category='material', year='永恒', tagline='纸的纤维。',
         description='通过模拟纸张的纹理(粗糙/颗粒/折痕/水渍),增加触觉感与真实感,是高端品牌、文创产品、有机品牌的常用手法。',
         characteristics=['纸纹理底', '折痕/水渍', '颗粒感', '触感强', '温暖'],
         colors=[('牛皮纸', '#c9a878'), ('宣纸', '#f5e8c7'), ('米色', '#e8dcc0')],
         typography='衬线/手写',
         useCases=['高端包装', '文创', '有机品牌'],
         examples=['Aesop', '无印良品'],
         visual='paper'),
    dict(id='frosted-glass', slug='frosted-glass', name='Frosted Glass', nameZh='毛玻璃',
         category='material', year='现代', tagline='朦胧的层次。',
         description='毛玻璃效果通过背景模糊 + 半透明实现,在 UI 中营造层次感与空间感,是 Apple 推动的现代界面语言。',
         characteristics=['半透明', '背景模糊', '细边框', '层次感', '高级'],
         colors=[('白半透明', 'rgba(255,255,255,0.2)'), ('彩色背景', '#7c3aed')],
         typography='现代无衬线',
         useCases=['iOS 界面', '音乐 App', '卡片叠加'],
         examples=['Apple Music', 'iOS 14+ Widgets'],
         visual='frost'),
    dict(id='metallic', slug='metallic', name='Metallic', nameZh='金属质感',
         category='material', year='古典', tagline='金属的反射。',
         description='金属质感通过渐变 + 高光 + 阴影模拟金/银/铜/铬的反射,营造奢华、未来、科技感,常用于高端品牌和游戏 UI。',
         characteristics=['金属渐变', '高光', '反射', '奢华', '未来感'],
         colors=[('金', '#d4af37'), ('银', '#c0c0c0'), ('铬蓝', '#a8c0d0')],
         typography='粗衬线/未来感',
         useCases=['奢侈品', '游戏', '高端品牌'],
         examples=['Cartier', 'YSL', 'Cyberpunk UI'],
         visual='metal'),
    dict(id='wood-grain', slug='wood-grain', name='Wood Grain', nameZh='木纹质感',
         category='material', year='永恒', tagline='树的年轮。',
         description='木纹质感模拟天然木材的纹理与色调,传达自然、温暖、可靠、手作感,常见于家居、咖啡、手工艺品牌。',
         characteristics=['木纹纹理', '暖色调', '自然感', '手作温度', '可靠'],
         colors=[('胡桃', '#5c3317'), ('橡木', '#c9a878'), ('松木', '#deb887')],
         typography='衬线/手写',
         useCases=['家居', '咖啡', '手工艺'],
         examples=['星巴克', '宜家'],
         visual='wood'),
    dict(id='water-ripple', slug='water-ripple', name='Water Ripple', nameZh='水波纹',
         category='material', year='永恒', tagline='水的呼吸。',
         description='模拟水波/涟漪的动态效果,传达流动、清新、平静的氛围,常见于水品牌、Spa、冥想类应用。',
         characteristics=['波纹', '蓝色调', '流动感', '清新', '平静'],
         colors=[('湖蓝', '#4a90a4'), ('浅蓝', '#a4c8e1'), ('白', '#ffffff')],
         typography='轻盈无衬线',
         useCases=['水/Spa 品牌', '冥想 App', '清新产品'],
         examples=['Spa 品牌', '矿泉水包装'],
         visual='water'),
    dict(id='fabric', slug='fabric', name='Fabric Texture', nameZh='织物质感',
         category='material', year='永恒', tagline='织物的温度。',
         description='模拟布料/织物纹理(亚麻/棉/丝绸/羊毛),传达温暖、舒适、手作品牌感,常见于服装、家居、手作品牌。',
         characteristics=['织物纹理', '温暖色调', '柔软感', '手作品牌', '舒适'],
         colors=[('亚麻', '#e8dcc0'), ('靛蓝', '#1e3a8a'), ('砖红', '#a82d2d')],
         typography='衬线/手写',
         useCases=['服装', '家居', '手作品牌'],
         examples=['Everlane', 'Patagonia'],
         visual='fabric'),

    # ===== 现代趋势 (10) =====
    dict(id='modern-tech', slug='modern-tech', name='Modern Tech', nameZh='现代科技',
         category='modern', year='2020s', tagline='深色与光晕。',
         description='2020 年代科技产品的视觉语言,以深色背景 + 渐变光晕 + 等宽字体 + 几何图形营造专业、前沿、神秘的氛围。',
         characteristics=['深色背景', '渐变光晕', '等宽字体', '几何装饰', '高科技感'],
         colors=[('深蓝', '#0a1628'), ('蓝', '#3b82f6'), ('紫', '#8b5cf6')],
         typography='Inter / SF Pro + JetBrains Mono',
         useCases=['AI 产品', 'SaaS', '开发者工具'],
         examples=['Linear', 'Vercel', 'Stripe'],
         visual='tech'),
    dict(id='editorial', slug='editorial', name='Editorial', nameZh='编辑设计',
         category='modern', year='2010s', tagline='杂志的呼吸。',
         description='源自杂志编辑设计的网页风格,以大字号衬线 + 强烈对比 + 精致排版 + Bento 网格为标志,常用于品牌故事、个人作品集。',
         characteristics=['大字号', '衬线体', 'Bento 网格', '强烈对比', '故事感'],
         colors=[('暖白', '#fafaf7'), ('黑', '#0a0a0a'), ('品牌色', '#c43e3e')],
         typography='衬线 + 无衬线混排',
         useCases=['品牌故事', '作品集', '长文阅读'],
         examples=['Bloomberg Businessweek', 'Pitchfork'],
         visual='editorial'),
    dict(id='nordic', slug='nordic', name='Nordic', nameZh='北欧极简',
         category='modern', year='1950s', tagline='冷与光的呼吸。',
         description='源自斯堪的纳维亚设计的北欧极简,以白底 + 柔和粉彩 + 大量留白 + 自然光为标志,营造明亮、舒适、生活的氛围。',
         characteristics=['大量留白', '柔和粉彩', '自然光', '功能性', '生活感'],
         colors=[('白', '#fafaf7'), ('淡粉', '#f5e6e0'), ('浅灰蓝', '#c8d5e0')],
         typography='现代无衬线,中等粗细',
         useCases=['家居', '生活方式', '北欧品牌'],
         examples=['IKEA', 'HAY', 'Aesop'],
         visual='nordic'),
    dict(id='dark-first', slug='dark-first', name='Dark First', nameZh='暗色优先',
         category='modern', year='2010s', tagline='暗夜为默认。',
         description='以暗色为默认主题的设计语言,通过减少光刺激、突出色彩对比,营造专业、专注、高级的氛围,是开发者工具和音乐产品的首选。',
         characteristics=['暗色背景', '高对比', '霓虹/品牌色点缀', '专注感', '专业'],
         colors=[('深灰', '#0a0a0a'), ('灰', '#1a1a1a'), ('品牌色', '#3b82f6')],
         typography='清晰无衬线',
         useCases=['开发者工具', '音乐 App', '游戏'],
         examples=['GitHub Dark', 'Spotify', 'Discord'],
         visual='dark'),
    dict(id='brutalism', slug='brutalism', name='Brutalism', nameZh='野兽派',
         category='modern', year='2010s', tagline='原始的诚实。',
         description='Web 上的野兽派(Brutalist Web)反对精致的商业化设计,以默认字体、原始 HTML 感、不对齐、冲突色彩为标志,体现"原始诚实"。',
         characteristics=['默认字体', '原始 HTML', '不对齐', '冲突色彩', 'DIY 感'],
         colors=[('亮黄', '#ffff00'), ('蓝', '#0000ff'), ('白', '#ffffff')],
         typography='默认 Times / Arial / Courier',
         useCases=['艺术家网站', '实验项目', 'Zine'],
         examples=['Bloomberg 早期', 'Are.na'],
         visual='brutal'),
    dict(id='magazine', slug='magazine', name='Magazine', nameZh='杂志风',
         category='modern', year='现代', tagline='卷轴的故事。',
         description='模仿印刷杂志的网页设计,以封面级大图 + 跨页布局 + 多栏排版 + 强烈字号对比为标志,适合长篇阅读和品牌故事。',
         characteristics=['大图封面', '多栏排版', '强烈字号', '跨页布局', '故事感'],
         colors=[('黑', '#0a0a0a'), ('白', '#ffffff'), ('品牌色', '#c43e3e')],
         typography='衬线 + 无衬线混排',
         useCases=['数字杂志', '长篇报道', '品牌故事'],
         examples=['The New York Times Magazine', 'National Geographic'],
         visual='magazine'),
    dict(id='flat-design', slug='flat-design', name='Flat Design', nameZh='扁平化设计',
         category='modern', year='2012', tagline='去除拟物。',
         description='2012 年微软 Metro 与苹果 iOS 7 推动的扁平化设计,反对拟物化的渐变/阴影,使用纯色 + 简洁图形,塑造现代移动 UI 语言。',
         characteristics=['纯色填充', '无渐变', '无阴影', '极简图形', '移动优先'],
         colors=[('亮蓝', '#2196f3'), ('红', '#f44336'), ('绿', '#4caf50')],
         typography='现代无衬线(Roboto)',
         useCases=['移动 App', '企业产品', '图标设计'],
         examples=['Windows 8 Metro', 'iOS 7', 'Google Material 1.0'],
         visual='flat'),
    dict(id='material-design', slug='material-design', name='Material Design', nameZh='材料设计',
         category='modern', year='2014', tagline='纸与影的逻辑。',
         description='2014 年 Google 推出的设计系统,以"纸 + 阴影"隐喻构建 UI,通过 Z 轴层级与动态动效,规范化 Android 与 Web 视觉语言。',
         characteristics=['卡片(Z轴)', '阴影层级', '涟漪效果', '鲜明色彩', '动效'],
         colors=[('Material 蓝', '#1976d2'), ('Material 红', '#d32f2f'), ('灰', '#f5f5f5')],
         typography='Roboto',
         useCases=['Android 应用', 'Web 应用', '跨平台产品'],
         examples=['Google Apps', 'Android 系统'],
         visual='material'),
    dict(id='3d-illustration', slug='3d-illustration', name='3D Illustration', nameZh='3D 插画',
         category='modern', year='2018', tagline='立体的表达。',
         description='2018 年后由 Spline、Blender 推动的 3D 插画,以柔和的色彩、夸张的造型、故事性场景成为 SaaS 与新消费品牌的视觉新语言。',
         characteristics=['3D 立体', '柔和色彩', '夸张造型', '故事性', '粘性高'],
         colors=[('柔粉', '#ffc1cc'), ('柔蓝', '#a4c8e1'), ('奶白', '#f5f0e8')],
         typography='圆润现代无衬线',
         useCases=['SaaS 落地页', '新消费品牌', '元宇宙'],
         examples=['Stripe 插画', 'Notion 3D', 'Pitch'],
         visual='3d'),
    dict(id='gradient-mesh', slug='gradient-mesh', name='Gradient Mesh', nameZh='渐变网格',
         category='modern', year='2020', tagline='色彩的地形。',
         description='渐变网格以多个色彩控制点模拟摄影般的色彩过渡,从 Figma/Apple 推动后成为现代 UI 与品牌设计的主流语言。',
         characteristics=['多色渐变', '柔和过渡', '现代感', '色彩丰富', '摄影感'],
         colors=[('紫', '#8b5cf6'), ('粉', '#ec4899'), ('青', '#06b6d4'), ('蓝', '#3b82f6')],
         typography='现代无衬线',
         useCases=['品牌识别', '英雄区', 'App 启动页'],
         examples=['iOS 14 壁纸', 'Instagram 渐变 logo'],
         visual='gradient'),
]

CATEGORIES = [
    dict(id='visual', name='视觉表现', nameEn='Visual Styles', desc='从极简到繁复的视觉语言', order=1),
    dict(id='eastern', name='东方古典', nameEn='Eastern Classical', desc='东方传统美学与现代设计的融合', order=2),
    dict(id='color', name='配色方案', nameEn='Color Schemes', desc='色彩的情感与象征', order=3),
    dict(id='typography', name='字体排版', nameEn='Typography', desc='字体的性格与节奏', order=4),
    dict(id='era', name='时代年代', nameEn='Era', desc='时代精神在视觉上的回响', order=5),
    dict(id='material', name='材质纹理', nameEn='Material', desc='触觉延伸到视觉', order=6),
    dict(id='modern', name='现代趋势', nameEn='Modern Trends', desc='当下与未来的设计语言', order=7),
]

ROOT = Path('docs/styles')

def colors_text(colors):
    """生成颜色代码块"""
    rows = []
    for name, hex_val in colors:
        rows.append(f"| {name} | `{hex_val}` | {'■' * 3} |")
    return '| 颜色名 | 十六进制 | 预览 |\n|--------|----------|------|\n' + '\n'.join(rows)

def style_page(s):
    """生成单个风格详情页"""
    cls = f"style-{s['slug']}"
    return f"""---
title: {s['nameZh']} - {s['name']}
sidebar_label: {s['nameZh']}
description: {s['description'][:80]}...
---

<div class="{cls}">

# {s['nameZh']}({s['name']})

> {s['tagline']}

**起源年代**: {s['year']} · **分类**: {next(c['name'] for c in CATEGORIES if c['id'] == s['category'])}

## 风格描述

{s['description']}

## 核心特征

{chr(10).join('- ' + c for c in s['characteristics'])}

## 配色方案

{colors_text(s['colors'])}

## 字体建议

{s['typography']}

## 适用场景

{chr(10).join('- ' + u for u in s['useCases'])}

## 代表案例

{chr(10).join('- ' + e for e in s['examples'])}

## 设计要点

设计 **{s['nameZh']}** 风格时,请记住:

1. **忠于核心特征** — 不要为了"看起来像 X"而堆砌装饰,而要让每个元素都为表达服务
2. **配色与字体协同** — 色彩与字体共同塑造风格情绪,任一改变都会削弱整体气质
3. **场景适配** — 即使是相同风格,在不同场景(网页/海报/包装)下的实现细节也不同
4. **时代背景** — 理解风格诞生的时代背景与文化土壤,避免无源之水的模仿

## 相关风格

浏览其他 **{next(c['name'] for c in CATEGORIES if c['id'] == s['category'])}** 分类下的设计风格,或查看完整 [风格目录](/all-styles)。

</div>
"""

def category_page(cat, styles):
    """生成单个分类索引页"""
    style_list = '\n'.join(f"- [{s['nameZh']} ({s['name']})](/styles/{cat['id']}/{s['slug']}) — *{s['tagline']}*" for s in styles)
    return f"""---
title: {cat['name']} - {cat['nameEn']}
sidebar_label: {cat['name']}
description: {cat['desc']}
---

# {cat['name']}({cat['nameEn']})

{cat['desc']}

本分类收录 **{len(styles)} 种** 设计风格。

## 风格列表

{style_list}

## 分类说明

**{cat['name']}** 关注{c['desc'][2:] if (c := cat)['desc'].startswith('色彩') or c['desc'].startswith('字体') or c['desc'].startswith('时代') or c['desc'].startswith('触觉') or c['desc'].startswith('当下') else c['desc']}。这些风格虽各有侧重,但都体现了人类对视觉表达的持续探索。

## 浏览其他分类

{chr(10).join(f"- [{c2['name']}](/styles/{c2['id']}) — {c2['desc']}" for c2 in CATEGORIES if c2['id'] != cat['id'])}
"""

# 写所有分类页和风格详情页
for cat in CATEGORIES:
    cat_dir = ROOT / cat['id']
    cat_dir.mkdir(parents=True, exist_ok=True)
    cat_styles = [s for s in STYLES if s['category'] == cat['id']]
    (cat_dir / 'index.md').write_text(category_page(cat, cat_styles), encoding='utf-8')
    for s in cat_styles:
        (cat_dir / f"{s['slug']}.md").write_text(style_page(s), encoding='utf-8')
    print(f"✓ {cat['name']}: {len(cat_styles)} 种风格")

print(f"\n总计: {len(STYLES)} 种风格,分布在 {len(CATEGORIES)} 个分类")
