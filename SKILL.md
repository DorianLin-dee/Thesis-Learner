---
name: "thesis_learner"
description: "论文学习助手 - 深度分析学术论文，提取关键内容，生成结构化分析报告"
---

# Thesis Learner - 论文学习助手

帮助您高效阅读和分析学术论文的智能工具，支持全文总述、章节分析、引用追踪和研究脉络梳理。

---

## 🎯 简洁工作流程（核心原则）

### 重要原则：忠于原文，不做推断
- **严禁**基于上下文做"合理推断/补全"论文章节、内容等
- **只使用**明确从WebFetch获取的内容或用户提供的PDF内容
- 如果WebFetch内容不完整，向用户说明局限性并请求更多信息

```
用户提供论文链接/DOI/标题
    ↓
WebFetch 读取网页内容（优先）
    ↓
    ├─ 如果内容完整 → 提取论文信息、章节结构、参考文献
    └─ 如果内容有限 → 向用户说明局限性，请求提供PDF或明确内容
    ↓
生成HTML分析报告（仅基于实际获取的内容）
```

---

# 论文搜索和总结助手

帮助您找到学术论文，获取免费版本，并生成清晰的总结和分析。

---

## 📚 核心功能

### 1. 论文搜索
- 使用多个免费学术数据库搜索论文
- 自动寻找免费PDF版本
- 支持标题、DOI、关键词搜索

### 2. 论文获取（优先网页读取）
- **WebFetch 优先**: 优先使用 WebFetch 读取论文网页内容
- **PDF 备选**: 仅在网页不可用时尝试下载PDF
- **免费来源**: arXiv、作者主页、Google Scholar、PubMed Central

### 3. 论文分析
- 提取摘要、关键词、研究方法
- 总结核心发现和结论
- 分析研究贡献和局限性
- 生成思维导图式结构

### 4. Related Work 分析 ⭐ 核心功能
- **自动提取**：从 PDF 自动识别并提取 Related Work 部分
- **引用提取**：自动识别 [Author Year] 格式的论文引用
- **免费链接**：为每篇论文搜索 DOI 和数据库链接
- **脉络梳理**：生成研究脉络思维导图
- **创新总结**：分析研究方向和创新点
- **格式规范**：引用论文表格包含「论文、年份、DOI、研究方向」四列，链接放在 DOI 列中

### 5. 完整论文分析 ⭐⭐ 新增
- **章节识别**：自动识别摘要、引言、相关工作、方法、实验、结论等所有章节
- **背景信息**：补充论文的研究背景和动机
- **引用追踪**：追踪每个章节的引用论文
- **结构分析**：分析论文的整体结构和逻辑
- **内容摘要**：为每个章节生成简洁摘要

### 6. 现代化多页面报告 ⭐⭐⭐ 新增
- **MacPaw 风格 UI**：简洁现代的设计语言
- **独立页面布局**：每个板块独立，左右翻页
- **交互式导航**：侧边栏 + 键盘快捷键
- **流畅动画**：平滑的页面切换效果
- **进度指示器**：清晰的当前位置指示
- **响应式设计**：支持多种设备

---

## 🚀 使用方式

### 基础使用
直接告诉我您需要什么论文：
- 论文标题
- 作者+标题
- DOI号
- 研究主题关键词

### 示例
```
"帮我找一下《Attention Is All You Need》这篇论文"
"搜索关于transformer在NLP中应用的论文"
"这是DOI: 10.48550/arXiv.1706.03762，帮我获取并总结"
```

### Related Work 分析使用方式 ⭐

**一句话搞定**（推荐）
```
"帮我分析论文 /path/to/paper.pdf 的 Related Work"
```

**工具自动完成：**
1. 📄 提取 PDF → 识别 Related Work → 提取引用
2. 🔍 搜索每篇论文的 DOI 和免费链接
3. 🧠 生成研究脉络思维导图
4. 💡 总结研究方向和创新点

**输出示例：**
- ✅ 识别 31 篇引用论文
- ✅ 识别 10 个研究主题
- ✅ 生成思维导图
- ✅ 提供免费链接表格

### 全文总述使用方式 ⭐⭐⭐（核心流程）

**一句话搞定**（推荐）
```
"帮我分析论文 /path/to/paper.pdf"
```

**工具自动完成：**
1. 📄 提取 PDF → 识别所有章节
2. 📝 生成**全文总述**（HTML格式）
3. 💬 等待用户指定要详细分析的章节

**全文总述包含 4 个板块：**
- 📋 **一、论文概览** - 基本信息、核心内容
- 📚 **二、章节结构** - 所有章节列表和简介
- 🔄 **三、工作流程** - 研究方法的核心步骤
- 🚀 **四、影响与展望** - 主要贡献、研究影响、未来方向

**输出示例：**
```
📄 论文基本信息
标题：[论文标题]
作者：[作者列表]
发表年份：[年份]
来源：[会议/期刊]

📋 全文总述已生成！
请告诉我您想详细分析哪个章节？
- Related Work（相关工作）
- Method（方法）
- Experiments（实验）
- Conclusion（结论）
- 其他特定章节...
```

### 特定章节分析使用方式 ⭐⭐

在获取全文总述后，用户可以指定要分析的章节：
```
"帮我分析 Related Work 部分"
"帮我详细看一下 Method 章节"
```

**工具自动完成：**
1. 📄 深度提取指定章节内容
2. 🔗 提取该章节的引用论文和免费链接
3. 🧠 生成该章节的专项分析报告

### 完整论文分析使用方式 ⭐⭐

如果用户一开始就要求分析全部内容：
```
"帮我分析论文 /path/to/paper.pdf 的全部内容"
```

**工具自动完成：**
1. 📄 提取 PDF → 识别所有章节
2. 📝 提取摘要、引言、方法、实验、结论
3. 🔍 补充背景信息和引用内容
4. 📊 分析论文结构和逻辑
5. 🧠 生成完整分析报告（HTML格式）

**输出示例：**
```
📄 论文结构
├── 1. 摘要 (Abstract)
├── 2. 引言 (Introduction) - 3 篇引用
├── 3. 相关工作 (Related Work) - 31 篇引用
├── 4. 方法 (Method) - 5 篇引用
├── 5. 实验 (Experiments) - 2 篇引用
└── 6. 结论 (Conclusion)

✅ 识别 6 个章节
✅ 提取 52 条参考文献
✅ 生成完整分析报告
```

**报告包含：**
- 📝 论文标题、作者、发表信息
- 📖 各章节内容摘要
- 🔗 参考文献免费链接
- 🧠 研究脉络思维导图
- 💡 核心贡献和创新点
- 📊 背景信息和动机

**多页面报告使用方式** ⭐⭐⭐

```
"帮我分析论文 /path/to/paper.pdf，生成现代化 HTML 报告"
```

**报告特点：**
- 🖥️ 6 个独立页面（概览、摘要、引言、相关工作、研究脉络、参考文献）
- ← → 左右翻页或点击侧边栏
- ⌨️ 键盘快捷键（方向键）
- 🎨 MacPaw 风格现代 UI
- 📱 响应式设计
- 🖨️ 支持打印成 PDF

---

## 🎨 HTML报告UI设计规范 ⭐⭐⭐⭐

### 核心依赖（必须引入）
每个 HTML 报告的 `<head>` 中必须包含：

```html
<script src="https://cdn.tailwindcss.com"></script>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,400;0,500;0,600;0,700;1,400;1,500;1,600&family=Noto+Sans+SC:wght@300;400;500;600;700&display=swap" rel="stylesheet">
```

### Tailwind 自定义配置
在 `<head>` 中添加 Tailwind 配置脚本：

```html
<script>
    tailwind.config = {
        theme: {
            extend: {
                fontFamily: {
                    serif: ['Cormorant Garamond', 'Georgia', 'serif'],
                    sans: ['Noto Sans SC', 'system-ui', 'sans-serif'],
                },
                colors: {
                    indigo: { 50: '#eef2ff', 100: '#e0e7ff', 200: '#c7d2fe', 300: '#a5b4fc', 400: '#818cf8', 500: '#6366f1', 600: '#4f46e5', 700: '#4338ca', 800: '#3730a3', 900: '#312e81', },
                    amber: { 50: '#fffbeb', 100: '#fef3c7', 200: '#fde68a', 300: '#fcd34d', 400: '#fbbf24', 500: '#f59e0b', 600: '#d97706', 700: '#b45309', 800: '#92400e', 900: '#78350f', },
                    teal: { 50: '#f0fdfa', 100: '#ccfbf1', 200: '#99f6e4', 300: '#5eead4', 400: '#2dd4bf', 500: '#14b8a6', 600: '#0d9488', 700: '#0f766e', 800: '#115e59', 900: '#134e4a', },
                    sky: { 50: '#f0f9ff', 100: '#e0f2fe', 200: '#bae6fd', 300: '#7dd3fc', 400: '#38bdf8', 500: '#0ea5e9', 600: '#0284c7', 700: '#0369a1', 800: '#075985', 900: '#0c4a6e', },
                    rose: { 50: '#fff1f2', 100: '#ffe4e6', 200: '#fecdd3', 300: '#fda4af', 400: '#fb7185', 500: '#f43f5e', 600: '#e11d48', 700: '#be123c', 800: '#9f1239', 900: '#881337', },
                },
            }
        }
    }
</script>
```

### 自定义 CSS 样式（必须添加到 `<style>` 标签）

```css
body { font-family: 'Noto Sans SC', system-ui, sans-serif; background: #fafaf9; color: #18181b; }
h1, h2, h3, h4, h5, h6 { font-family: 'Cormorant Garamond', Georgia, serif; }
.font-serif { font-family: 'Cormorant Garamond', Georgia, serif; }
.font-sans { font-family: 'Noto Sans SC', system-ui, sans-serif; }

/* 卡片进场动画 */
.fade-up { opacity: 0; transform: translateY(20px); transition: opacity 0.7s ease, transform 0.7s ease, box-shadow 0.3s ease; }
.fade-up.show { opacity: 1; transform: translateY(0); }

/* 顶部阅读进度条 */
.scroll-bar { position: fixed; top: 0; left: 0; height: 3px; z-index: 9999; background: linear-gradient(90deg, #6366f1 0%, #8b5cf6 50%, #ec4899 100%); }

/* 右侧悬浮圆点导航 */
.side-nav { position: fixed; right: 24px; top: 50%; transform: translateY(-50%); z-index: 50; display: flex; flex-direction: column; gap: 12px; }
.side-nav-item { width: 10px; height: 10px; border-radius: 50%; background: rgba(148, 163, 184, 0.4); cursor: pointer; transition: all 0.3s ease; position: relative; }
.side-nav-item:hover { background: rgba(99, 102, 241, 0.6); transform: scale(1.3); }
.side-nav-item.active { background: #6366f1; width: 24px; border-radius: 5px; }
.side-nav-item span { position: absolute; right: 24px; top: 50%; transform: translateY(-50%); background: rgba(255,255,255,0.95); padding: 6px 12px; border-radius: 8px; font-size: 12px; color: #334155; white-space: nowrap; opacity: 0; pointer-events: none; transition: opacity 0.3s ease; box-shadow: 0 4px 12px rgba(0,0,0,0.1); }
.side-nav-item:hover span { opacity: 1; }

/* 回到顶部按钮 */
.to-top-btn { position: fixed; right: 24px; bottom: 24px; z-index: 50; width: 48px; height: 48px; border-radius: 50%; background: white; box-shadow: 0 4px 20px rgba(0,0,0,0.12); display: flex; align-items: center; justify-content: center; cursor: pointer; opacity: 0; visibility: hidden; transition: all 0.3s ease; }
.to-top-btn.show { opacity: 1; visibility: visible; }
.to-top-btn:hover { transform: translateY(-3px); box-shadow: 0 6px 24px rgba(0,0,0,0.15); }

/* 模块背景大数字 */
.mod-bg-num { font-family: 'Cormorant Garamond', Georgia, serif; font-size: clamp(100px, 15vw, 180px); font-weight: 700; opacity: 0.04; position: absolute; top: -20px; right: -20px; line-height: 1; pointer-events: none; }

/* 标签 Tag */
.tag { display: inline-flex; align-items: center; gap: 4px; padding: 4px 12px; border-radius: 100px; font-size: 11px; font-weight: 500; background: rgba(99, 102, 241, 0.1); color: #4f46e5; }

/* 分割线 */
.divider { height: 1px; background: linear-gradient(90deg, transparent, rgba(99, 102, 241, 0.3), transparent); margin: 48px 0; }

/* 背景装饰圆 */
.orb { position: absolute; border-radius: 50%; filter: blur(80px); opacity: 0.15; pointer-events: none; }

/* 讲座卡片 */
.lecture-card { background: white; border: 1px solid #f4f4f5; border-radius: 16px; padding: 24px; transition: all 0.3s ease; }
.lecture-card:hover { transform: translateY(-3px); box-shadow: 0 12px 40px rgba(99, 102, 241, 0.12); border-color: rgba(99, 102, 241, 0.15); }

/* 自定义滚动条 */
::-webkit-scrollbar { width: 6px; }
::-webkit-scrollbar-track { background: #f1f5f9; }
::-webkit-scrollbar-thumb { background: #cbd5e1; border-radius: 3px; }
::-webkit-scrollbar-thumb:hover { background: #94a3b8; }
```

### 五大配色主题约定
每个报告模块使用独立配色，约定如下：

| 模块序号 | 主题色 | CSS类 | 使用场景 |
|---------|--------|-------|---------|
| 01 | indigo 紫蓝 | `text-indigo-600`, `bg-indigo-100` | 论文概览、封面 |
| 02 | amber 琥珀 | `text-amber-500`, `bg-amber-100` | 引用论文、章节 |
| 03 | teal 青绿 | `text-teal-500`, `bg-teal-100` | 研究脉络、方法论 |
| 04 | sky 天蓝 | `text-sky-500`, `bg-sky-100` | 实验结果、数据 |
| 05 | rose 玫瑰 | `text-rose-500`, `bg-rose-100` | 总结、展望 |

### 字体层次约定
- **大标题 Hero**：`text-4xl md:text-6xl lg:text-7xl font-bold font-serif`
- **模块标题**：`text-3xl md:text-4xl font-bold font-serif`
- **卡片标题**：`text-xl font-semibold text-zinc-900`
- **正文**：`text-sm text-zinc-600 leading-relaxed`
- **次要文字**：`text-zinc-500`

### JavaScript 交互逻辑（添加到 `<script>` 标签底部）

```javascript
// 阅读进度条 + 回到顶部按钮 + 导航高亮
const scrollBar = document.getElementById('scrollBar');
const toTopBtn = document.getElementById('toTopBtn');
const sideNavItems = document.querySelectorAll('.side-nav-item');
const sections = document.querySelectorAll('section');

window.addEventListener('scroll', () => {
    const scrollTop = window.scrollY;
    const docHeight = document.documentElement.scrollHeight - window.innerHeight;
    const scrollPercent = (scrollTop / docHeight) * 100;
    scrollBar.style.width = scrollPercent + '%';

    if (scrollTop > 500) toTopBtn.classList.add('show');
    else toTopBtn.classList.remove('show');

    sections.forEach(section => {
        const sectionTop = section.offsetTop - 100;
        const sectionHeight = section.offsetHeight;
        if (scrollTop >= sectionTop && scrollTop < sectionTop + sectionHeight) {
            sideNavItems.forEach(item => item.classList.remove('active'));
            const activeItem = document.querySelector(`.side-nav-item[data-section="${section.id}"]`);
            if (activeItem) activeItem.classList.add('active');
        }
    });
});

toTopBtn.addEventListener('click', () => window.scrollTo({ top: 0, behavior: 'smooth' }));

sideNavItems.forEach(item => {
    item.addEventListener('click', () => {
        const sectionId = item.getAttribute('data-section');
        const section = document.getElementById(sectionId);
        if (section) section.scrollIntoView({ behavior: 'smooth' });
    });
});

// 卡片进场动画
const fadeCards = document.querySelectorAll('.fade-up');
const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
        if (entry.isIntersecting) entry.target.classList.add('show');
    });
}, { threshold: 0.1, rootMargin: '0px 0px -50px 0px' });
fadeCards.forEach(card => observer.observe(card));
```

---

## 📄 全文总述 HTML 格式规范 ⭐⭐⭐

### 整体结构约定
全文总述是一个单页滚动式 HTML，包含 Hero 封面 + 4 个主要模块。每个模块使用独立的主题色。

| 模块 | 内容 | 主题色 | Section ID |
|------|------|--------|------------|
| Hero | 封面、论文标题、标签、统计卡片 | indigo | `hero` |
| 01 | 论文概览（基本信息、核心内容） | indigo | `overview` |
| 02 | 章节结构（所有章节列表与简介） | amber | `structure` |
| 03 | 工作流程（方法的核心步骤） | teal | `workflow` |
| 04 | 影响与展望（贡献、价值、未来方向） | rose | `impact` |

### 右侧导航配置
```html
<div class="side-nav" id="sideNav">
    <div class="side-nav-item active" data-section="hero"><span>封面</span></div>
    <div class="side-nav-item" data-section="overview"><span>概览</span></div>
    <div class="side-nav-item" data-section="structure"><span>章节</span></div>
    <div class="side-nav-item" data-section="workflow"><span>流程</span></div>
    <div class="side-nav-item" data-section="impact"><span>展望</span></div>
</div>
```

### Hero 封面结构
```html
<section id="hero" class="relative min-h-[60vh] flex items-center justify-center py-20 overflow-hidden">
    <div class="orb w-[400px] h-[400px] bg-indigo-500 top-[-100px] left-[-100px]"></div>
    <div class="orb w-[300px] h-[300px] bg-purple-500 bottom-[-50px] right-[100px]"></div>
    <div class="orb w-[250px] h-[250px] bg-rose-400 top-[100px] right-[-50px]"></div>

    <div class="relative z-10 text-center px-6 max-w-4xl mx-auto">
        <div class="flex justify-center gap-3 mb-6 flex-wrap">
            <span class="tag">论文分析</span>
            <span class="tag bg-amber-100 text-amber-700">Research</span>
            <span class="tag bg-teal-100 text-teal-700">Analysis</span>
        </div>
        <h1 class="text-4xl md:text-6xl lg:text-7xl font-bold font-serif text-zinc-900 mb-6 leading-tight">
            [论文标题]<span class="text-indigo-600 italic">分析</span>
        </h1>
        <p class="text-lg md:text-xl text-zinc-500 font-light max-w-2xl mx-auto mb-8">[作者 · 年份 · 来源]</p>
        <div class="flex justify-center gap-6 flex-wrap">
            <div class="bg-white/80 backdrop-blur-sm rounded-2xl px-6 py-4 shadow-lg">
                <div class="text-3xl font-bold text-indigo-600 font-serif">[章节数]</div>
                <div class="text-sm text-zinc-500">章节</div>
            </div>
            <div class="bg-white/80 backdrop-blur-sm rounded-2xl px-6 py-4 shadow-lg">
                <div class="text-3xl font-bold text-amber-500 font-serif">[引用数]</div>
                <div class="text-sm text-zinc-500">引用</div>
            </div>
            <div class="bg-white/80 backdrop-blur-sm rounded-2xl px-6 py-4 shadow-lg">
                <div class="text-3xl font-bold text-teal-500 font-serif">[贡献数]</div>
                <div class="text-sm text-zinc-500">核心贡献</div>
            </div>
        </div>
    </div>
</section>
```

### 模块通用结构
每个模块的标准结构（以 01 概览为例，其他模块替换颜色即可）：
```html
<div class="divider"></div>

<section id="overview" class="py-16 px-6 md:px-12 lg:px-24 max-w-6xl mx-auto">
    <div class="relative mb-12">
        <h2 class="text-3xl md:text-4xl font-bold font-serif text-zinc-900 mb-4">
            <span class="text-indigo-600">01</span> 论文概览
        </h2>
        <p class="text-zinc-500 max-w-xl">论文基本信息与核心内容</p>
        <span class="mod-bg-num text-indigo-600">01</span>
    </div>

    <div class="grid md:grid-cols-2 gap-6">
        <div class="lecture-card fade-up">
            <div class="flex items-start gap-4">
                <div class="w-10 h-10 rounded-full bg-indigo-100 flex items-center justify-center flex-shrink-0">
                    <!-- icon -->
                </div>
                <div>
                    <h3 class="text-xl font-semibold text-zinc-900 mb-2">[标题]</h3>
                    <p class="text-zinc-600 text-sm leading-relaxed">[内容]</p>
                </div>
            </div>
        </div>
        <!-- 更多卡片 -->
    </div>

    <div class="mt-8 lecture-card fade-up">
        <h3 class="text-xl font-semibold text-zinc-900 mb-4">[摘要/核心发现]</h3>
        <p class="text-zinc-600 leading-relaxed">[内容]</p>
    </div>
</section>
```

### 章节结构模块样式（带数字序号）
```html
<div class="space-y-3">
    <div class="flex items-start gap-4 bg-white rounded-2xl p-5 border border-zinc-100 fade-up">
        <div class="w-10 h-10 rounded-xl bg-amber-100 flex items-center justify-center flex-shrink-0 text-amber-600 font-semibold text-sm">01</div>
        <div class="flex-1">
            <h4 class="text-lg font-semibold text-zinc-900 mb-1">Introduction（引言）</h4>
            <p class="text-sm text-zinc-600 leading-relaxed">介绍研究背景和动机</p>
        </div>
    </div>
    <!-- 更多章节 -->
</div>
```

### 工作流程模块样式（时间线风格）
```html
<div class="relative pl-16">
    <div class="absolute left-[22px] top-0 bottom-0 w-0.5 bg-teal-200"></div>

    <div class="relative mb-8 fade-up">
        <div class="absolute -left-[40px] w-11 h-11 rounded-full bg-gradient-to-br from-teal-400 to-teal-600 text-white flex items-center justify-center font-bold shadow-lg shadow-teal-500/30">1</div>
        <div class="bg-white rounded-2xl p-5 border border-zinc-100">
            <h4 class="text-lg font-semibold text-zinc-900 mb-2">[步骤标题]</h4>
            <p class="text-sm text-zinc-600 leading-relaxed">[步骤描述]</p>
        </div>
    </div>
    <!-- 更多步骤 -->
</div>
```

### 各模块颜色替换规则
| 模块 | 需替换的颜色类 | 示例 |
|------|--------------|------|
| 01 概览 | indigo | `text-indigo-600`, `bg-indigo-100` |
| 02 章节 | amber | `text-amber-500`, `bg-amber-100` |
| 03 流程 | teal | `text-teal-500`, `bg-teal-100` |
| 04 展望 | rose | `text-rose-500`, `bg-rose-100` |

---

## 📊 输出格式

```
📄 论文基本信息
标题：[论文标题]
作者：[作者列表]
发表年份：[年份]
来源：[会议/期刊]

🎯 核心贡献
1. [贡献1]
2. [贡献2]
...

🔬 研究方法
[方法概述]

📈 主要发现
1. [发现1]
2. [发现2]
...

💡 总结与启示
[总结内容]

📎 获取链接
[可用的免费链接]
```

---

## 🛠️ 配套脚本

### paper_search.py - 论文搜索工具
搜索论文并寻找免费PDF链接。

```bash
python3 .trae/skills/paper_finder/paper_search.py "论文标题"
```

### pdf_extractor.py - PDF内容提取
从PDF文件中提取文本内容。

```bash
python3 .trae/skills/paper_finder/pdf_extractor.py "论文.pdf"
```

### paper_summarizer.py - 论文总结
分析和总结论文内容。

```bash
python3 .trae/skills/paper_finder/paper_summarizer.py "论文.pdf"
```

### related_work_analyzer.py - Related Work 分析 ⭐
分析 PDF 论文的 Related Work 部分。

```bash
python3 .trae/skills/paper_finder/related_work_analyzer.py "paper.pdf"
```

**功能：** 自动提取 → 提取引用 → 搜索链接 → 生成报告

### full_paper_analyzer.py - 完整论文分析 ⭐⭐
分析 PDF 论文的全部章节。

```bash
python3 .trae/skills/paper_finder/full_paper_analyzer.py "paper.pdf"
```

**功能：** 识别所有章节 → 提取引用 → 生成结构化分析 → 输出 JSON 报告

**章节识别原则（重要！）：
- **严格遵循原文**: 必须从论文网页/PDF中提取真实章节标题，不要臆造
- **严禁推断**: 如果WebFetch或PDF没有提供完整章节，向用户说明局限性，不要补全
- **完整列表**: 根据原文实际列出所有章节
- **中英文对照**: 提供原文标题 + 中文翻译
- **准确描述**: 每个章节的描述要基于该章节的实际内容

**常见章节示例（仅作参考，以实际原文为准）：**
- Abstract（摘要）
- Introduction（引言）
- Related Work（相关工作）
- Background（背景）
- Method/Approach（方法）
- Implementation（实现）
- Experiments/Results（实验/结果）
- Conclusion（结论）

---

## 🔍 搜索策略

### WebFetch 局限性说明
- WebFetch通常只能获取论文网页的基本信息（摘要、参考文献等）
- 如果需要完整内容（章节结构、技术细节），需要用户提供PDF
- 遇到内容不完整时，要向用户说明，而不是自己推断补全

### 优先查找顺序
1. **arXiv.org** - 检查是否有预印本
2. **作者个人主页** - 许多学者会放自己论文
3. **Google Scholar** - 查看"All versions"
4. **PubMed Central** - 生物医学领域
5. **Sci-Hub/LibGen** - 作为备选方案

### 提示技巧
- 尽量使用完整准确的标题
- 有DOI优先使用DOI
- 加上作者名字可以提高准确率
- 如果WebFetch内容不完整，请求用户提供PDF文件

---

## ⚠️ 完整HTML示例代码 ⚠️（必看）

以下是完整的HTML模板，必须严格遵循此格式，避免常见错误：

### 完整HTML结构示例

```html
<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>论文分析报告</title>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,400;0,500;0,600;0,700;1,400;1,500;1,600&family=Noto+Sans+SC:wght@300;400;500;600;700&display=swap" rel="stylesheet">
    <script src="https://cdn.tailwindcss.com"></script>
    <script src="https://unpkg.com/lucide@latest"></script>
    <script>
        tailwind.config = {
            theme: {
                extend: {
                    fontFamily: {
                        serif: ['Cormorant Garamond', 'Georgia', 'serif'],
                        sans: ['Noto Sans SC', 'system-ui', 'sans-serif'],
                    },
                    colors: {
                        indigo: { 50: '#eef2ff', 100: '#e0e7ff', 200: '#c7d2fe', 300: '#a5b4fc', 400: '#818cf8', 500: '#6366f1', 600: '#4f46e5', 700: '#4338ca', 800: '#3730a3', 900: '#312e81', },
                        amber: { 50: '#fffbeb', 100: '#fef3c7', 200: '#fde68a', 300: '#fcd34d', 400: '#fbbf24', 500: '#f59e0b', 600: '#d97706', 700: '#b45309', 800: '#92400e', 900: '#78350f', },
                        teal: { 50: '#f0fdfa', 100: '#ccfbf1', 200: '#99f6e4', 300: '#5eead4', 400: '#2dd4bf', 500: '#14b8a6', 600: '#0d9488', 700: '#0f766e', 800: '#115e59', 900: '#134e4a', },
                        sky: { 50: '#f0f9ff', 100: '#e0f2fe', 200: '#bae6fd', 300: '#7dd3fc', 400: '#38bdf8', 500: '#0ea5e9', 600: '#0284c7', 700: '#0369a1', 800: '#075985', 900: '#0c4a6e', },
                        rose: { 50: '#fff1f2', 100: '#ffe4e6', 200: '#fecdd3', 300: '#fda4af', 400: '#fb7185', 500: '#f43f5e', 600: '#e11d48', 700: '#be123c', 800: '#9f1239', 900: '#881337', },
                    },
                }
            }
        }
    </script>
    <style>
        body { font-family: 'Noto Sans SC', system-ui, sans-serif; }
        h1, h2, h3, h4, h5, h6 { font-family: 'Cormorant Garamond', Georgia, serif; }
        .font-serif { font-family: 'Cormorant Garamond', Georgia, serif; }
        .font-sans { font-family: 'Noto Sans SC', system-ui, sans-serif; }
        
        .fade-up { opacity: 0; transform: translateY(20px); transition: opacity 0.7s ease, transform 0.7s ease, box-shadow 0.3s ease; }
        .fade-up.show { opacity: 1; transform: translateY(0); }
        
        .scroll-bar { position: fixed; top: 0; left: 0; height: 3px; z-index: 9999; background: linear-gradient(90deg, #6366f1 0%, #8b5cf6 50%, #ec4899 100%); }
        
        .side-nav { position: fixed; right: 24px; top: 50%; transform: translateY(-50%); z-index: 50; display: flex; flex-direction: column; gap: 12px; }
        
        .side-nav-item { width: 10px; height: 10px; border-radius: 50%; background: rgba(148, 163, 184, 0.4); cursor: pointer; transition: all 0.3s ease; position: relative; }
        .side-nav-item:hover { background: rgba(99, 102, 241, 0.6); transform: scale(1.3); }
        .side-nav-item.active { background: #6366f1; width: 24px; border-radius: 5px; }
        
        .side-nav-item span { position: absolute; right: 24px; top: 50%; transform: translateY(-50%); background: rgba(255,255,255,0.95); padding: 6px 12px; border-radius: 8px; font-size: 12px; color: #334155; white-space: nowrap; opacity: 0; pointer-events: none; transition: opacity 0.3s ease; box-shadow: 0 4px 12px rgba(0,0,0,0.1); }
        .side-nav-item:hover span { opacity: 1; }
        
        .to-top-btn { position: fixed; right: 24px; bottom: 24px; z-index: 50; width: 48px; height: 48px; border-radius: 50%; background: white; box-shadow: 0 4px 20px rgba(0,0,0,0.12); display: flex; align-items: center; justify-content: center; cursor: pointer; opacity: 0; visibility: hidden; transition: all 0.3s ease; }
        .to-top-btn.show { opacity: 1; visibility: visible; }
        .to-top-btn:hover { transform: translateY(-3px); box-shadow: 0 6px 24px rgba(0,0,0,0.15); }
        
        .mod-bg-num { font-family: 'Cormorant Garamond', Georgia, serif; font-size: clamp(100px, 15vw, 180px); font-weight: 700; opacity: 0.04; position: absolute; top: -20px; right: -20px; line-height: 1; pointer-events: none; }
        
        .tag { display: inline-flex; align-items: center; gap: 4px; padding: 4px 12px; border-radius: 100px; font-size: 11px; font-weight: 500; background: rgba(99, 102, 241, 0.1); color: #4f46e5; }
        
        .divider { height: 1px; background: linear-gradient(90deg, transparent, rgba(99, 102, 241, 0.3), transparent); margin: 48px 0; }
        
        .orb { position: absolute; border-radius: 50%; filter: blur(80px); opacity: 0.15; pointer-events: none; }
        
        .lecture-card { background: white; border: 1px solid #f4f4f5; border-radius: 16px; padding: 24px; transition: all 0.3s ease; }
        .lecture-card:hover { transform: translateY(-3px); box-shadow: 0 12px 40px rgba(99, 102, 241, 0.12); border-color: rgba(99, 102, 241, 0.15); }
        
        ::-webkit-scrollbar { width: 6px; }
        ::-webkit-scrollbar-track { background: #f1f5f9; }
        ::-webkit-scrollbar-thumb { background: #cbd5e1; border-radius: 3px; }
        ::-webkit-scrollbar-thumb:hover { background: #94a3b8; }
    </style>
</head>
<body class="bg-stone-50 text-zinc-800 min-h-screen">
    <div class="scroll-bar" id="scrollBar"></div>
    
    <div class="side-nav" id="sideNav">
        <div class="side-nav-item active" data-section="hero"><span>封面</span></div>
        <div class="side-nav-item" data-section="overview"><span>概览</span></div>
        <div class="side-nav-item" data-section="papers"><span>引用论文</span></div>
        <div class="side-nav-item" data-section="mindmap"><span>思维导图</span></div>
    </div>
    
    <button class="to-top-btn" id="toTopBtn">
        <i data-lucide="chevron-up" class="w-5 h-5 text-zinc-600"></i>
    </button>

    <div class="relative">
        <section id="hero" class="relative min-h-[60vh] flex items-center justify-center py-20 overflow-hidden">
            <div class="orb w-[400px] h-[400px] bg-indigo-500 top-[-100px] left-[-100px]"></div>
            <div class="orb w-[300px] h-[300px] bg-purple-500 bottom-[-50px] right-[100px]"></div>
            <div class="orb w-[250px] h-[250px] bg-rose-400 top-[100px] right-[-50px]"></div>
            
            <div class="relative z-10 text-center px-6 max-w-4xl mx-auto">
                <div class="flex justify-center gap-3 mb-6 flex-wrap">
                    <span class="tag">论文分析</span>
                    <span class="tag bg-amber-100 text-amber-700">Research</span>
                    <span class="tag bg-teal-100 text-teal-700">Analysis</span>
                </div>
                <h1 class="text-4xl md:text-6xl lg:text-7xl font-bold font-serif text-zinc-900 mb-6 leading-tight">
                    论文分析<span class="text-indigo-600 italic">报告</span>
                </h1>
                <p class="text-lg md:text-xl text-zinc-500 font-light max-w-2xl mx-auto mb-8">
                    深入分析学术论文，提取引用脉络，构建研究思维导图
                </p>
                <div class="flex justify-center gap-6 flex-wrap">
                    <div class="bg-white/80 backdrop-blur-sm rounded-2xl px-6 py-4 shadow-lg">
                        <div class="text-3xl font-bold text-indigo-600 font-serif">0</div>
                        <div class="text-sm text-zinc-500">引用论文</div>
                    </div>
                    <div class="bg-white/80 backdrop-blur-sm rounded-2xl px-6 py-4 shadow-lg">
                        <div class="text-3xl font-bold text-amber-500 font-serif">0</div>
                        <div class="text-sm text-zinc-500">研究主题</div>
                    </div>
                    <div class="bg-white/80 backdrop-blur-sm rounded-2xl px-6 py-4 shadow-lg">
                        <div class="text-3xl font-bold text-teal-500 font-serif">0</div>
                        <div class="text-sm text-zinc-500">核心贡献</div>
                    </div>
                </div>
                <div class="mt-12 animate-bounce">
                    <i data-lucide="chevron-down" class="w-8 h-8 text-zinc-400 mx-auto"></i>
                </div>
            </div>
        </section>

        <div class="divider"></div>

        <section id="overview" class="py-16 px-6 md:px-12 lg:px-24 max-w-6xl mx-auto">
            <div class="relative mb-12">
                <h2 class="text-3xl md:text-4xl font-bold font-serif text-zinc-900 mb-4">
                    <span class="text-indigo-600">01</span> 论文概览
                </h2>
                <p class="text-zinc-500 max-w-xl">目标论文基本信息与核心内容</p>
                <span class="mod-bg-num text-indigo-600">01</span>
            </div>
            
            <div class="grid md:grid-cols-2 gap-6">
                <div class="lecture-card fade-up">
                    <div class="flex items-start gap-4">
                        <div class="w-10 h-10 rounded-full bg-indigo-100 flex items-center justify-center flex-shrink-0">
                            <i data-lucide="file-text" class="w-5 h-5 text-indigo-600"></i>
                        </div>
                        <div>
                            <h3 class="text-xl font-semibold text-zinc-900 mb-2">论文标题</h3>
                            <p class="text-zinc-600 text-sm leading-relaxed">[论文标题内容]</p>
                        </div>
                    </div>
                </div>
                
                <div class="lecture-card fade-up">
                    <div class="flex items-start gap-4">
                        <div class="w-10 h-10 rounded-full bg-amber-100 flex items-center justify-center flex-shrink-0">
                            <i data-lucide="users" class="w-5 h-5 text-amber-600"></i>
                        </div>
                        <div>
                            <h3 class="text-xl font-semibold text-zinc-900 mb-2">作者信息</h3>
                            <p class="text-zinc-600 text-sm leading-relaxed">[作者列表]</p>
                        </div>
                    </div>
                </div>
                
                <div class="lecture-card fade-up">
                    <div class="flex items-start gap-4">
                        <div class="w-10 h-10 rounded-full bg-teal-100 flex items-center justify-center flex-shrink-0">
                            <i data-lucide="calendar" class="w-5 h-5 text-teal-600"></i>
                        </div>
                        <div>
                            <h3 class="text-xl font-semibold text-zinc-900 mb-2">发表信息</h3>
                            <p class="text-zinc-600 text-sm leading-relaxed">[期刊/会议信息]</p>
                        </div>
                    </div>
                </div>
                
                <div class="lecture-card fade-up">
                    <div class="flex items-start gap-4">
                        <div class="w-10 h-10 rounded-full bg-sky-100 flex items-center justify-center flex-shrink-0">
                            <i data-lucide="link" class="w-5 h-5 text-sky-600"></i>
                        </div>
                        <div>
                            <h3 class="text-xl font-semibold text-zinc-900 mb-2">文献链接</h3>
                            <p class="text-zinc-600 text-sm leading-relaxed">[DOI / 链接]</p>
                        </div>
                    </div>
                </div>
            </div>
            
            <div class="mt-8 lecture-card fade-up">
                <h3 class="text-xl font-semibold text-zinc-900 mb-4">研究摘要</h3>
                <p class="text-zinc-600 leading-relaxed">[摘要内容]</p>
            </div>
        </section>

        <div class="divider"></div>

        <section id="papers" class="py-16 px-6 md:px-12 lg:px-24 max-w-6xl mx-auto">
            <div class="relative mb-12">
                <h2 class="text-3xl md:text-4xl font-bold font-serif text-zinc-900 mb-4">
                    <span class="text-amber-500">02</span> 引用论文
                </h2>
                <p class="text-zinc-500 max-w-xl">引用论文完整列表与分类</p>
                <span class="mod-bg-num text-amber-500">02</span>
            </div>
            
            <div class="space-y-4">
                <div class="lecture-card fade-up">
                    <div class="flex items-start gap-4">
                        <div class="w-8 h-8 rounded-full bg-amber-100 flex items-center justify-center flex-shrink-0">
                            <span class="text-xs font-bold text-amber-600">01</span>
                        </div>
                        <div class="flex-1">
                            <h3 class="text-lg font-semibold text-zinc-900 mb-1">[论文标题]</h3>
                            <p class="text-sm text-zinc-500 mb-2">[作者, Year]</p>
                            <p class="text-sm text-zinc-600 leading-relaxed">[摘要片段]</p>
                        </div>
                        <a href="#" class="text-indigo-600 hover:text-indigo-700 flex-shrink-0">
                            <i data-lucide="external-link" class="w-5 h-5"></i>
                        </a>
                    </div>
                </div>
            </div>
        </section>

        <div class="divider"></div>

        <section id="mindmap" class="py-16 px-6 md:px-12 lg:px-24 max-w-6xl mx-auto">
            <div class="relative mb-12">
                <h2 class="text-3xl md:text-4xl font-bold font-serif text-zinc-900 mb-4">
                    <span class="text-teal-500">03</span> 研究脉络
                </h2>
                <p class="text-zinc-500 max-w-xl">思维导图式研究演进</p>
                <span class="mod-bg-num text-teal-500">03</span>
            </div>
            
            <div class="lecture-card fade-up">
                <div class="font-mono text-sm text-zinc-600 leading-relaxed whitespace-pre-wrap">
研究脉络
├─ 主题1
│   ├─ Author [Year]
│   └─ Author [Year]
├─ 主题2
│   ├─ Author [Year]
│   └─ Author [Year]
└─ 主题3
    └─ Author [Year]
                </div>
            </div>
        </section>

        <div class="divider"></div>

        <footer class="py-12 text-center text-zinc-400 text-sm">
            <p>论文分析报告 · Generated by Paper Finder Skill</p>
        </footer>
    </div>

    <script>
        lucide.createIcons();
        
        const scrollBar = document.getElementById('scrollBar');
        const toTopBtn = document.getElementById('toTopBtn');
        const sideNavItems = document.querySelectorAll('.side-nav-item');
        const sections = document.querySelectorAll('section');
        
        window.addEventListener('scroll', () => {
            const scrollTop = window.scrollY;
            const docHeight = document.documentElement.scrollHeight - window.innerHeight;
            const scrollPercent = (scrollTop / docHeight) * 100;
            scrollBar.style.width = scrollPercent + '%';
            
            if (scrollTop > 500) {
                toTopBtn.classList.add('show');
            } else {
                toTopBtn.classList.remove('show');
            }
            
            sections.forEach(section => {
                const sectionTop = section.offsetTop - 100;
                const sectionHeight = section.offsetHeight;
                if (scrollTop >= sectionTop && scrollTop < sectionTop + sectionHeight) {
                    sideNavItems.forEach(item => item.classList.remove('active'));
                    const activeItem = document.querySelector(`.side-nav-item[data-section="${section.id}"]`);
                    if (activeItem) activeItem.classList.add('active');
                }
            });
        });
        
        toTopBtn.addEventListener('click', () => {
            window.scrollTo({ top: 0, behavior: 'smooth' });
        });
        
        sideNavItems.forEach(item => {
            item.addEventListener('click', () => {
                const sectionId = item.getAttribute('data-section');
                const section = document.getElementById(sectionId);
                if (section) {
                    section.scrollIntoView({ behavior: 'smooth' });
                }
            });
        });
        
        const fadeCards = document.querySelectorAll('.fade-up');
        const observer = new IntersectionObserver((entries) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    entry.target.classList.add('show');
                }
            });
        }, { threshold: 0.1, rootMargin: '0px 0px -50px 0px' });
        
        fadeCards.forEach(card => observer.observe(card));
    </script>
</body>
</html>
```

---

## 🚨 常见错误与避免方法 🚨

### 1. Tailwind CDN 未引入
**错误原因**：忘记在 `<head>` 中引入 `https://cdn.tailwindcss.com`
**避免方法**：每个 HTML 文件的 `<head>` 中必须包含 Tailwind CDN 脚本和自定义配置

### 2. 字体未加载（显示系统默认字体）
**错误原因**：缺少 Google Fonts 的 Cormorant Garamond 和 Noto Sans SC 引入
**避免方法**：确保 `<head>` 中有 fonts.googleapis.com 和 fonts.gstatic.com 的 preconnect + link

### 3. 模块颜色不一致
**错误原因**：同一模块混用了不同主题色（如 02 章节模块中出现 indigo）
**避免方法**：严格遵循配色约定表（01-indigo / 02-amber / 03-teal / 04-sky / 05-rose）

### 4. 动画元素缺少 fade-up 类
**错误原因**：卡片没有添加 `fade-up` 类，导致进场动画失效
**避免方法**：所有 `.lecture-card` 和主要卡片都必须添加 `fade-up` 类

### 5. Section ID 与导航 data-section 不匹配
**错误原因**：`section id="xxx"` 与 `side-nav-item data-section="xxx"` 不一致
**避免方法**：section ID 必须与对应导航项的 data-section 完全一致

### 6. 阅读进度条不显示
**错误原因**：缺少 `scroll-bar` 元素或缺少对应 CSS
**避免方法**：`<body>` 后必须立即放置 `<div class="scroll-bar" id="scrollBar"></div>`

### 7. 回到顶部按钮不工作
**错误原因**：缺少 to-top-btn 元素或 JavaScript 脚本
**避免方法**：确保有 `<button class="to-top-btn" id="toTopBtn">` + 对应的 scroll 事件监听

---

## ✅ 检查清单

每次生成HTML报告后，必须检查以下项目：

- [ ] Tailwind CDN：已在 `<head>` 引入 `https://cdn.tailwindcss.com`
- [ ] Tailwind 自定义配置：已添加 5 套主题色（indigo/amber/teal/sky/rose）
- [ ] 字体：已引入 Cormorant Garamond 和 Noto Sans SC
- [ ] 阅读进度条：`<div class="scroll-bar" id="scrollBar">` 存在，渐变色正确
- [ ] 右侧导航：`.side-nav` 存在，每个 `.side-nav-item` 有正确的 `data-section`
- [ ] 回到顶部按钮：`.to-top-btn` 存在，滚动 500px 后显示
- [ ] Hero 封面：至少有 3 个 `.orb` 装饰圆，有 `tag` 标签，有统计卡片
- [ ] 模块标题：每个 section 有 `.mod-bg-num` 大数字背景装饰
- [ ] 卡片动画：所有主要卡片包含 `fade-up` 类
- [ ] 分割线：每个 section 之间有 `<div class="divider"></div>`
- [ ] Section ID：hero / overview / structure / workflow / impact 与导航项一一对应
- [ ] 主题色一致性：01-indigo / 02-amber / 03-teal / 04-rose
- [ ] JavaScript：已包含 scroll 监听、to-top 点击、fade-up IntersectionObserver 三段代码
- [ ] body 样式：`bg-stone-50 text-zinc-800 min-h-screen`
