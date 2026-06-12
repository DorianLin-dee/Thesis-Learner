---
name: "thesis_reader"
description: "论文阅读与分析助手 - 生成全文总述、章节分析、Related Work研究脉络思维导图"
---

# 论文分析与报告生成助手

简洁可泛化的论文分析工具，从网页读取论文内容，生成专业的HTML分析报告。

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

### 整体布局
- **左侧导航栏**：默认隐藏，鼠标移到最左侧（50px内）时滑出显示
- **底部导航栏**：默认隐藏，鼠标移到最底部（50px内）时滑出显示
- **顶部标题卡片**：作为页面内容的一部分，随内容滚动，不固定在顶部
- **浅蓝渐变背景**：`linear-gradient(135deg, #E3F2FD 0%, #BBDEFB 100%)`

### 导航栏样式
#### 左侧导航栏
- **默认隐藏**：`transform: translateX(-100%)`
- **鼠标在左侧50px内显示**：`transform: translateX(0)`
- **鼠标移出隐藏**
- **毛玻璃背景**：`rgba(255, 255, 255, 0.95)` + `backdrop-filter: blur(20px)`
- **阴影**：`0 0 20px rgba(0,0,0,0.1)`
- **过渡动画**：`transition: transform 0.3s ease`
- **position**: fixed, top: 0, left: 0, bottom: 0, z-index: 1000

#### 底部导航栏
- **默认隐藏**：`transform: translateY(100%)`
- **鼠标在底部50px内显示**：`transform: translateY(0)`
- **鼠标移出隐藏**
- **毛玻璃背景**：同上
- **阴影**：`0 -4px 24px rgba(0,0,0,0.1)`
- **position**: fixed, left: 0, right: 0, bottom: 0, z-index: 999
- **⚠️ 重要**：不要使用 `body:hover .pagination` 这样的选择器，这会导致底部导航栏一直显示

### 内容区样式
- **背景**：透明 `transparent`
- **顶部标题栏**：毛玻璃背景 + `backdrop-filter: blur(20px)`
- **内容区背景**：透明，让渐变背景透出

### JavaScript导航栏逻辑
```javascript
// 获取导航栏元素
const sidebar = document.querySelector('.sidebar');
const pagination = document.querySelector('.pagination');

// 鼠标移动事件
document.addEventListener('mousemove', function(e) {
    // 左侧50px内显示侧边栏
    if (e.clientX < 50) {
        sidebar.classList.add('visible');
    } else if (!sidebar.matches(':hover')) {
        sidebar.classList.remove('visible');
    }

    // 底部50px内显示底部导航栏
    if (e.clientY > window.innerHeight - 50) {
        pagination.classList.add('visible');
    } else if (!pagination.matches(':hover')) {
        pagination.classList.remove('visible');
    }
});

// 悬停在导航栏时保持显示
if (sidebar) {
    sidebar.addEventListener('mouseenter', () => sidebar.classList.add('visible'));
    sidebar.addEventListener('mouseleave', () => sidebar.classList.remove('visible'));
}

if (pagination) {
    pagination.addEventListener('mouseenter', () => pagination.classList.add('visible'));
    pagination.addEventListener('mouseleave', () => pagination.classList.remove('visible'));
}
```

### 标题卡片样式
作为内容的一部分，每个页面顶部都有一个标题卡片：
- **圆角矩形**：16px圆角
- **内边距**：24px
- **居中对齐**：text-align: center
- **阴影**：`0 4px 24px rgba(0,0,0,0.08)`
- **悬停动画**：向上移动4px + 阴影增强
- **字体层次**：
  - 主标题(h2)：24px，字重700，颜色`#1D1D1F`
  - 副标题(p)：13px，字重正常，颜色`#86868B`
- **内容处理**：超出宽度时显示省略号

### 统计卡片样式（概览页面信息卡片）
用于展示论文核心研究主题，**大标题在上，小标签在下**：
- **圆角**：16px
- **内边距**：24px
- **居中对齐**
- **布局**：上方显示研究主题内容（蓝色大字），下方显示类别标签（灰色小字）
- **大标题样式**（`.stat-number`）：
  - 字号：20px
  - 字重：700
  - 颜色：`#007AFF`（主题蓝）
  - 行高：1.3
  - 允许换行显示
- **小标签样式**（`.stat-label`）：
  - 字号：13px
  - 字重：600
  - 颜色：`#86868B`
  - 大写转换：`text-transform: uppercase`
  - 字母间距：`letter-spacing: 0.5px`
- **悬停动画**：向上移动4px + 阴影增强

**示例结构**：
```html
<div class="stat-card">
    <div class="stat-number">可编程负泊松比超材料</div>
    <div class="stat-label">材料</div>
</div>
```

### 通用卡片样式
- **圆角**：16px
- **内边距**：32px
- **阴影**：`0 4px 24px rgba(0,0,0,0.08)`
- **悬停阴影**：`0 8px 32px rgba(0,0,0,0.12)`
- **过渡**：0.3秒 ease

### 颜色变量
```css
:root {
    --primary: #007AFF;        /* 主题蓝 */
    --primary-dark: #0056CC;   /* 深蓝 */
    --bg: #FFFFFF;             /* 白色 */
    --bg-secondary: #F5F5F7;  /* 浅灰背景 */
    --text: #1D1D1F;           /* 主文字 */
    --text-secondary: #86868B; /* 次要文字 */
    --border: #E5E5E7;         /* 边框 */
    --card-shadow: 0 4px 24px rgba(0,0,0,0.08);
    --hover-shadow: 0 8px 32px rgba(0,0,0,0.12);
}
```

### 内容溢出处理
所有文本内容都要防止溢出：
```css
overflow: hidden;
text-overflow: ellipsis;
white-space: nowrap;
```

### 时间线样式
```css
.timeline {
    position: relative;
    padding-left: 40px;
}

.timeline::before {
    content: "";
    position: absolute;
    left: 15px;
    top: 0;
    bottom: 0;
    width: 2px;
    background: linear-gradient(180deg, var(--primary), var(--bg-secondary));
}

.timeline-item {
    position: relative;
    margin-bottom: 24px;
    padding: 20px;
    background: var(--bg);
    border-radius: 12px;
    box-shadow: var(--card-shadow);
}

.timeline-item::before {
    content: "";
    position: absolute;
    left: -31px;
    top: 24px;
    width: 12px;
    height: 12px;
    background: var(--primary);
    border-radius: 50%;
    border: 3px solid var(--bg);
    box-shadow: 0 0 0 3px var(--primary);
}

.timeline-step {
    font-size: 14px;
    font-weight: 700;
    color: var(--primary);
    margin-bottom: 6px;
}

.timeline-title {
    font-size: 16px;
    font-weight: 600;
    margin-bottom: 8px;
}

.timeline-desc {
    font-size: 14px;
    color: var(--text-secondary);
}
```

### 页面切换动画
```css
@keyframes fadeIn {
    from { opacity: 0; transform: translateY(10px); }
    to { opacity: 1; transform: translateY(0); }
}
```

---

## 📄 全文总述 HTML 格式规范 ⭐⭐⭐

### 页面结构
全文总述是一个单页面 HTML，包含 4 个主要板块。在概览页面中，首先显示论文基本信息卡片，然后是其他内容。

### 论文基本信息卡片
在概览页面的开始位置，必须包含论文基本信息卡片，包含以下信息：
- 英文标题
- 中文标题
- 作者列表
- 会议/期刊信息
- 机构信息

示例格式：
```html
<div class="card">
    <div class="card-header">
        <div class="card-icon">📄</div>
        <div>
            <div class="card-title">Rapid Deployment of Curved Surfaces via Programmable Auxetics</div>
            <div class="card-subtitle">通过可编程负泊松比材料快速部署曲面</div>
        </div>
    </div>
    <div style="font-size: 14px; color: var(--text-secondary); margin-top: 16px;">
        <p style="margin-bottom: 12px;"><strong>作者：</strong>Jian Li, Hsueh-Cheng Wang, ...</p>
        <p style="margin-bottom: 12px;"><strong>会议：</strong>SIGGRAPH 2020</p>
        <p style="margin-bottom: 12px;"><strong>DOI：</strong><a href="https://doi.org/10.1145/3388769.3403368" target="_blank" style="color: var(--primary);">10.1145/3388769.3403368</a></p>
        <p><strong>机构：</strong>卡内基梅隆大学，...</p>
    </div>
</div>
```

### 章节结构规范
论文章节列表中，摘要（Abstract）必须是第一个章节，使用"0"作为编号标识，而不是数字"1"。后续章节编号从"1"开始。

示例：
```html
<div class="chapter-card">
    <div class="chapter-number">0</div>
    <div class="chapter-content">
        <div class="chapter-title">ABSTRACT (摘要)</div>
        <div class="chapter-desc">概述研究目标、方法和主要贡献。</div>
    </div>
</div>
<div class="chapter-card">
    <div class="chapter-number">1</div>
    <div class="chapter-content">
        <div class="chapter-title">INTRODUCTION (引言)</div>
        <div class="chapter-desc">介绍研究背景和动机。</div>
    </div>
</div>
```

```html
<div class="card">
    <div class="card-header">
        <div class="card-icon">📋</div>
        <div>
            <div class="card-title">一、论文概览</div>
            <div class="card-subtitle">论文基本信息与核心内容</div>
        </div>
    </div>
    <!-- 内容 -->
</div>

<div class="card">
    <div class="card-header">
        <div class="card-icon">📚</div>
        <div>
            <div class="card-title">二、章节结构</div>
            <div class="card-subtitle">论文组织结构</div>
        </div>
    </div>
    <!-- 内容 -->
</div>

<div class="card">
    <div class="card-header">
        <div class="card-icon">🔄</div>
        <div>
            <div class="card-title">三、工作流程</div>
            <div class="card-subtitle">方法的核心步骤</div>
        </div>
    </div>
    <!-- 内容 -->
</div>

<div class="card">
    <div class="card-header">
        <div class="card-icon">🚀</div>
        <div>
            <div class="card-title">四、影响与展望</div>
            <div class="card-subtitle">研究价值与未来方向</div>
        </div>
    </div>
    <!-- 内容 -->
</div>
```

### 章节结构板块样式
使用带数字序号的章节列表：
```html
<div class="chapter-item">
    <div class="chapter-number">1</div>
    <div class="chapter-content">
        <h4>Introduction（引言）</h4>
        <p>介绍研究背景和动机</p>
    </div>
</div>
```

### 工作流程板块样式
使用时间线风格的流程展示：
```html
<div class="workflow-step">
    <div class="workflow-left">
        <div class="workflow-dot">1</div>
        <div class="workflow-line"></div>
    </div>
    <div class="workflow-right">
        <h4>问题定义</h4>
        <p>明确研究问题</p>
    </div>
</div>
```

### 统计卡片完整 CSS 示例
```css
.stats-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
    gap: 20px;
    margin-bottom: 32px;
}

.stat-card {
    background: var(--bg);
    border-radius: 16px;
    padding: 24px;
    text-align: center;
    box-shadow: var(--card-shadow);
    transition: all 0.3s ease;
}

.stat-card:hover {
    transform: translateY(-4px);
    box-shadow: var(--hover-shadow);
}

.stat-number {
    font-size: 20px;
    font-weight: 700;
    color: var(--primary);
    line-height: 1.3;
    margin-bottom: 8px;
}

.stat-label {
    font-size: 13px;
    color: var(--text-secondary);
    font-weight: 600;
    text-transform: uppercase;
    letter-spacing: 0.5px;
}
```

### 概览页面完整 HTML 示例
```html
<!-- 统计卡片区域 -->
<div class="stats-grid">
    <div class="stat-card">
        <div class="stat-number">可编程负泊松比超材料</div>
        <div class="stat-label">材料</div>
    </div>
    <div class="stat-card">
        <div class="stat-number">共形几何设计</div>
        <div class="stat-label">方法</div>
    </div>
    <div class="stat-card">
        <div class="stat-number">充气/重力驱动</div>
        <div class="stat-label">驱动</div>
    </div>
    <div class="stat-card">
        <div class="stat-number">医疗/建筑/航天</div>
        <div class="stat-label">应用</div>
    </div>
</div>

<!-- 研究目标卡片 -->
<div class="card">
    <div class="card-header">
        <div class="card-icon">🎯</div>
        <div>
            <div class="card-title">研究目标</div>
            <div class="card-subtitle">开发可快速部署的双曲面可编程结构</div>
        </div>
    </div>
    <p style="font-size: 15px; line-height: 1.8; color: var(--text); margin-bottom: 16px;">
        本论文的核心目标是...
    </p>
    <ul style="font-size: 14px; line-height: 1.8; color: var(--text-secondary); margin: 20px 0 20px 24px;">
        <li style="margin-bottom: 10px;">关键要点1</li>
        <li style="margin-bottom: 10px;">关键要点2</li>
    </ul>
</div>

<!-- 研究范畴卡片 -->
<div class="card">
    <div class="card-header">
        <div class="card-icon">🏷️</div>
        <div class="card-title">研究范畴</div>
    </div>
    <div style="margin: 20px 0;">
        <span class="tag">计算机图形学</span>
        <span class="tag">计算制造</span>
        <span class="tag">可展开结构</span>
    </div>
</div>
```

---

## 📊 输出格式

```
📄 论文基本信息
标题：[论文标题]
中文标题：[论文中文标题]
作者：[作者列表]
发表年份：[年份]
来源：[会议/期刊]
机构：[机构信息]

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
    <style>
        /* ===== 基础样式 ===== */
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        :root {
            --primary: #007AFF;
            --primary-dark: #0056CC;
            --bg: #FFFFFF;
            --bg-secondary: #F5F5F7;
            --text: #1D1D1F;
            --text-secondary: #86868B;
            --border: #E5E5E7;
            --card-shadow: 0 4px 24px rgba(0,0,0,0.08);
            --hover-shadow: 0 8px 32px rgba(0,0,0,0.12);
        }

        body {
            font-family: -apple-system, BlinkMacSystemFont, "SF Pro Display", "Segoe UI", Roboto, sans-serif;
            background: linear-gradient(135deg, #E3F2FD 0%, #BBDEFB 100%);
            color: var(--text);
            line-height: 1.6;
            overflow: hidden;
            height: 100vh;
        }

        /* ===== 左侧导航栏 ===== */
        .sidebar {
            width: 280px;
            background: rgba(255,255,255,0.95);
            backdrop-filter: blur(20px);
            border-right: 1px solid var(--border);
            display: flex;
            flex-direction: column;
            position: fixed;
            top: 0;
            left: 0;
            bottom: 0;
            z-index: 1000;
            transform: translateX(-100%);
            transition: transform 0.3s ease;
            box-shadow: 0 0 20px rgba(0,0,0,0.1);
        }

        .sidebar.visible {
            transform: translateX(0);
        }

        .sidebar-header {
            padding: 24px;
            border-bottom: 1px solid var(--border);
        }

        .sidebar-header h1 {
            font-size: 18px;
            font-weight: 700;
            color: var(--text);
            margin-bottom: 8px;
        }

        .sidebar-header p {
            font-size: 13px;
            color: var(--text-secondary);
        }

        .nav-menu {
            flex: 1;
            padding: 16px 12px;
            overflow-y: auto;
        }

        .nav-item {
            display: flex;
            align-items: center;
            padding: 12px 16px;
            margin: 4px 0;
            border-radius: 10px;
            cursor: pointer;
            transition: all 0.2s ease;
            font-size: 14px;
            color: var(--text);
        }

        .nav-item:hover {
            background: var(--bg-secondary);
        }

        .nav-item.active {
            background: var(--primary);
            color: white;
            font-weight: 500;
        }

        /* ===== 内容区 ===== */
        .content {
            flex: 1;
            display: flex;
            flex-direction: column;
            background: transparent;
            overflow: hidden;
            margin-left: 0;
        }

        .content-body {
            flex: 1;
            padding: 32px 48px;
            overflow-y: auto;
            background: transparent;
        }

        /* ===== 标题卡片 ===== */
        .title-card {
            background: var(--bg);
            border-radius: 16px;
            padding: 24px;
            margin-bottom: 24px;
            box-shadow: var(--card-shadow);
            transition: all 0.3s ease;
            text-align: center;
        }

        .title-card:hover {
            transform: translateY(-4px);
            box-shadow: var(--hover-shadow);
        }

        .title-card h2 {
            font-size: 24px;
            font-weight: 700;
            color: var(--text);
            margin-bottom: 8px;
        }

        .title-card p {
            font-size: 13px;
            color: var(--text-secondary);
        }

        /* ===== 底部导航栏 ===== */
        .pagination {
            display: flex;
            justify-content: space-between;
            align-items: center;
            padding: 24px 48px;
            background: rgba(255, 255, 255, 0.95);
            backdrop-filter: blur(20px);
            border-top: 1px solid var(--border);
            position: fixed;
            left: 0;
            right: 0;
            bottom: 0;
            z-index: 999;
            transform: translateY(100%);
            transition: transform 0.3s ease;
            box-shadow: 0 -4px 24px rgba(0,0,0,0.1);
        }

        .pagination.visible {
            transform: translateY(0);
        }

        /* ===== 页面 ===== */
        .page {
            display: none;
            animation: fadeIn 0.4s ease;
        }

        .page.active {
            display: block;
        }

        @keyframes fadeIn {
            from { opacity: 0; transform: translateY(10px); }
            to { opacity: 1; transform: translateY(0); }
        }

        /* ===== 卡片 ===== */
        .card {
            background: var(--bg);
            border-radius: 16px;
            padding: 32px;
            margin-bottom: 24px;
            box-shadow: var(--card-shadow);
            transition: all 0.3s ease;
        }

        .card:hover {
            box-shadow: var(--hover-shadow);
        }

        .card-header {
            display: flex;
            align-items: center;
            margin-bottom: 24px;
        }

        .card-icon {
            width: 48px;
            height: 48px;
            background: linear-gradient(135deg, var(--primary), var(--primary-dark));
            border-radius: 12px;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 24px;
            margin-right: 16px;
        }

        .card-title {
            font-size: 20px;
            font-weight: 600;
            color: var(--text);
        }

        /* ===== 统计卡片 ===== */
        .stats-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
            gap: 20px;
            margin-bottom: 32px;
        }

        .stat-card {
            background: var(--bg);
            border-radius: 16px;
            padding: 24px;
            text-align: center;
            box-shadow: var(--card-shadow);
            transition: all 0.3s ease;
        }

        .stat-card:hover {
            transform: translateY(-4px);
            box-shadow: var(--hover-shadow);
        }

        .stat-number {
            font-size: 32px;
            font-weight: 600;
            color: var(--primary);
            line-height: 1;
            margin-bottom: 8px;
        }

        .stat-label {
            font-size: 13px;
            color: var(--text-secondary);
            font-weight: 500;
        }

        /* ===== 页面指示器 ===== */
        .page-indicator {
            display: flex;
            gap: 8px;
        }

        .dot {
            width: 8px;
            height: 8px;
            border-radius: 50%;
            background: var(--border);
            transition: all 0.3s ease;
        }

        .dot.active {
            background: var(--primary);
            width: 24px;
            border-radius: 4px;
        }

        .nav-btn {
            display: flex;
            align-items: center;
            gap: 8px;
            padding: 12px 24px;
            background: var(--bg);
            border: 1px solid var(--border);
            border-radius: 10px;
            cursor: pointer;
            font-size: 14px;
            font-weight: 500;
            color: var(--text);
            transition: all 0.2s ease;
        }

        .nav-btn:hover {
            background: var(--primary);
            color: white;
            border-color: var(--primary);
        }

        .nav-btn:disabled {
            opacity: 0.3;
            cursor: not-allowed;
        }

        .nav-btn:disabled:hover {
            background: var(--bg);
            color: var(--text);
            border-color: var(--border);
        }
    </style>
</head>
<body>
    <div class="app">
        <!-- ===== 左侧导航栏 ===== -->
        <div class="sidebar">
            <div class="sidebar-header">
                <h1>📚 论文分析</h1>
                <p>完整分析报告</p>
            </div>
            <div class="nav-menu">
                <div class="nav-item active" data-page="overview">
                    <span class="icon">🏠</span>
                    <span>概览</span>
                </div>
                <div class="nav-item" data-page="papers">
                    <span class="icon">📄</span>
                    <span>引用论文</span>
                </div>
                <div class="nav-item" data-page="mindmap">
                    <span class="icon">🧠</span>
                    <span>思维导图</span>
                </div>
            </div>
        </div>

        <!-- ===== 内容区 ===== -->
        <div class="content">
            <div class="content-body">
                <!-- 页面1: 概览 -->
                <div class="page active" id="page-overview">
                    <div class="title-card">
                        <h2>论文概览</h2>
                        <p>目标论文基本信息</p>
                    </div>
                    <!-- 内容在这里 -->
                </div>

                <!-- 页面2: 引用论文 -->
                <div class="page" id="page-papers">
                    <div class="title-card">
                        <h2>引用论文</h2>
                        <p>引用论文完整列表</p>
                    </div>
                    <!-- 内容在这里 -->
                </div>

                <!-- 页面3: 思维导图 -->
                <div class="page" id="page-mindmap">
                    <div class="title-card">
                        <h2>思维导图</h2>
                        <p>研究脉络梳理</p>
                    </div>
                    <!-- 内容在这里 -->
                </div>
            </div>

            <!-- ===== 底部导航栏 ===== -->
            <div class="pagination">
                <button class="nav-btn" id="prev-btn" disabled>← 上一页</button>
                <div class="page-indicator">
                    <div class="dot active" data-page="overview"></div>
                    <div class="dot" data-page="papers"></div>
                    <div class="dot" data-page="mindmap"></div>
                </div>
                <button class="nav-btn" id="next-btn">下一页 →</button>
            </div>
        </div>
    </div>

    <script>
        // ===== 页面配置 =====
        const pages = ['overview', 'papers', 'mindmap'];
        let currentPage = 0;

        // ===== 页面切换函数 =====
        function goToPage(index) {
            if (index < 0 || index >= pages.length) return;

            // 切换页面显示
            document.querySelectorAll('.page').forEach(p => p.classList.remove('active'));
            const targetPage = document.getElementById(`page-${pages[index]}`);
            if (targetPage) {
                targetPage.classList.add('active');
            }

            // 更新左侧导航栏选中状态
            document.querySelectorAll('.nav-item').forEach(n => n.classList.remove('active'));
            const activeNavItem = document.querySelector(`.nav-item[data-page="${pages[index]}"]`);
            if (activeNavItem) {
                activeNavItem.classList.add('active');
            }

            // 更新页面指示器
            document.querySelectorAll('.dot').forEach(d => d.classList.remove('active'));
            const activeDot = document.querySelector(`.dot[data-page="${pages[index]}"]`);
            if (activeDot) {
                activeDot.classList.add('active');
            }

            // 更新按钮状态
            document.getElementById('prev-btn').disabled = index === 0;
            document.getElementById('next-btn').disabled = index === pages.length - 1;

            currentPage = index;
        }

        // ===== 事件监听 =====
        document.getElementById('prev-btn').addEventListener('click', () => goToPage(currentPage - 1));
        document.getElementById('next-btn').addEventListener('click', () => goToPage(currentPage + 1));

        document.querySelectorAll('.nav-item').forEach(item => {
            item.addEventListener('click', () => {
                const page = item.getAttribute('data-page');
                goToPage(pages.indexOf(page));
            });
        });

        document.querySelectorAll('.dot').forEach(dot => {
            dot.addEventListener('click', () => {
                const page = dot.getAttribute('data-page');
                goToPage(pages.indexOf(page));
            });
        });

        // 键盘导航
        document.addEventListener('keydown', (e) => {
            if (e.key === 'ArrowLeft' || e.key === 'ArrowUp') {
                goToPage(currentPage - 1);
            } else if (e.key === 'ArrowRight' || e.key === 'ArrowDown' || e.key === ' ') {
                goToPage(currentPage + 1);
            }
        });

        // ===== 导航栏显示/隐藏逻辑 =====
        const sidebar = document.querySelector('.sidebar');
        const pagination = document.querySelector('.pagination');

        document.addEventListener('mousemove', function(e) {
            // 左侧50px内显示侧边栏
            if (e.clientX < 50) {
                sidebar.classList.add('visible');
            } else if (!sidebar.matches(':hover')) {
                sidebar.classList.remove('visible');
            }

            // 底部50px内显示底部导航栏
            if (e.clientY > window.innerHeight - 50) {
                pagination.classList.add('visible');
            } else if (!pagination.matches(':hover')) {
                pagination.classList.remove('visible');
            }
        });

        // 悬停在导航栏时保持显示
        if (sidebar) {
            sidebar.addEventListener('mouseenter', () => sidebar.classList.add('visible'));
            sidebar.addEventListener('mouseleave', () => sidebar.classList.remove('visible'));
        }

        if (pagination) {
            pagination.addEventListener('mouseenter', () => pagination.classList.add('visible'));
            pagination.addEventListener('mouseleave', () => pagination.classList.remove('visible'));
        }
    </script>
</body>
</html>
```

---

## 🚨 常见错误与避免方法 🚨

### 1. 底部导航栏一直显示
**错误原因**：使用了 `body:hover .pagination` 或类似选择器
**避免方法**：只使用 `.pagination.visible` 类控制显示

### 2. 左侧导航栏选中不变色
**错误原因**：
- 缺少 `.nav-item.active` 样式
- JavaScript代码中没有正确添加/移除 `active` 类
- 元素不存在但没有进行空值检查
**避免方法**：
- 确保有 `.nav-item.active` 样式定义
- JavaScript中使用 `if (element) { ... }` 进行空值检查

### 3. 页面标题更新失败
**错误原因**：尝试更新不存在的ID
**避免方法**：
- 每个页面都有自己的标题卡片（`.title-card`）
- 不需要动态更新标题，每个页面的标题都直接写在HTML中

### 4. 元素选择器找不到元素
**错误原因**：ID或类名拼写错误，或元素不存在
**避免方法**：
- 使用 `querySelector` 后总是检查返回值是否为 `null`
- 使用 `if (element) { ... }` 包裹操作代码

### 5. 页面结构不一致
**错误原因**：部分页面有标题卡片，部分页面没有
**避免方法**：**所有页面**都必须有 `.title-card` 作为第一个元素

---

## ✅ 检查清单

每次生成HTML报告后，必须检查以下项目：

- [ ] 左侧导航栏：鼠标移到左侧50px内显示，移出隐藏
- [ ] 左侧导航栏：点击某个项目后，该项目有蓝色背景高亮
- [ ] 底部导航栏：鼠标移到底部50px内显示，移出隐藏
- [ ] 底部导航栏：**不会**因为鼠标在页面其他位置就一直显示
- [ ] 所有页面：都有 `.title-card` 作为第一个元素
- [ ] 页面切换：左侧导航栏选中状态、页面指示器状态同步更新
- [ ] 统计卡片：数字大小为32px，字重600
- [ ] 页面切换：有淡入动画效果
- [ ] 背景：浅蓝渐变 `linear-gradient(135deg, #E3F2FD 0%, #BBDEFB 100%)`
- [ ] JavaScript：所有元素选择都有空值检查

---

## 📁 完整HTML样本文件

以下是两个完整的HTML样本文件路径，生成报告时应以此为参考：

### 1. 全文总述样本
文件路径：`/Users/dorian/Documents/solo/Paper/rapid_deployment_full_paper_overview.html`

**特点**：
- 4个页面：论文概览、章节结构、工作流程、影响与展望
- 论文基本信息卡片（标题、作者、会议、DOI、机构）
- 章节编号从"0"（摘要）开始
- 统计卡片展示核心研究主题
- 时间线展示工作流程
- 应用前景板块使用emoji图标

### 2. Related Work分析样本
文件路径：`/Users/dorian/Documents/solo/Paper/related_work_complete.html`

**特点**：
- 6个页面：概览、引用论文、思维导图、方法对比、研究脉络、关键洞察
- 统计卡片展示研究主题数量、引用论文数量等
- 数据表格展示引用论文（论文名、年份、DOI/链接、简介）
- 思维导图包含7大研究领域，每个领域下有"经验"和"问题"两个部分
- 使用缩进和边框展示内容层级
- 重点论文用橙色⭐标记
- 时间线展示2010-2018年研究演进
- 关键洞察板块总结研究趋势和技术演进
