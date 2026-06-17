---
name: "paper-related-work"
description: "分析学术论文的 Related Work 部分，提取引用论文，搜索免费链接，生成 Tailwind 风格的 HTML 研究脉络报告"
---

# Related Work 分析助手

自动分析学术论文的 Related Work 部分，提取引用论文信息，生成 Tailwind CSS 现代风格的 HTML 研究脉络报告。

---

## 🎨 UI 设计规范（Tailwind CSS 现代风格，⭐ 必须遵守）

### 核心设计原则
- **Tailwind CSS CDN**：所有 HTML 必须通过 `<script src="https://cdn.tailwindcss.com">` 引入
- **字体系统**：Cormorant Garamond（衬线标题） + Noto Sans SC（中文正文）
- **背景**：`bg-stone-50` 米色背景 + `text-zinc-800` 深灰文字
- **卡片**：`bg-white rounded-2xl border border-zinc-100` 基础卡片样式
- **模块配色**：每大板块一个主题色（indigo 紫蓝 / emerald 翠绿 / amber 琥珀 / sky 天蓝 / rose 玫瑰）
- **大序号装饰**：每个模块左上角有 `.mod-bg-num` 大数字背景（Cormorant 字体，半透明）

### 顶部交互元素
```html
<!-- 顶部阅读进度条 -->
<div class="scroll-bar" style="position:fixed;top:0;left:0;height:3px;z-index:9999;background:linear-gradient(90deg,#6366f1,#8b5cf6,#ec4899);"></div>

<!-- 右侧悬浮导航 -->
<div class="side-nav" style="position:fixed;right:24px;top:50%;transform:translateY(-50%);z-index:50;display:flex;flex-direction:column;gap:12px;">
    <div class="side-nav-item" data-section="module1" style="width:10px;height:10px;border-radius:50%;background:rgba(148,163,184,0.4);cursor:pointer;"></div>
</div>

<!-- 回到顶部按钮 -->
<button class="to-top-btn" style="position:fixed;right:24px;bottom:24px;z-index:50;width:48px;height:48px;border-radius:50%;background:white;box-shadow:0 4px 20px rgba(0,0,0,0.12);display:flex;align-items:center;justify-content:center;cursor:pointer;opacity:0;visibility:hidden;transition:all 0.3s ease;">↑</button>
```

### Hero 封面区结构
每个报告开头必须有 Hero 封面：
- 3 个模糊装饰圆（`.orb`）：`position:absolute;filter:blur(80px);opacity:0.15;`
- 标题：`text-4xl md:text-6xl font-bold font-serif`
- 标签 chip：`.tag` (padding:4px 12px, border-radius:100px, font-size:11px)
- 3 张统计卡：`bg-white/80 backdrop-blur-sm rounded-2xl`

### 讲座/章节卡片样式
- 每个章节用圆形编号徽章（N01/N02/L01/L02 等）
- 徽章：`w-12 h-12 rounded-xl bg-gradient-to-br from-indigo-500 to-violet-600 text-white flex items-center justify-center font-bold font-serif text-lg shadow-lg shadow-indigo-200`
- 卡片主体：`lecture-card fade-up`，带 hover 抬升效果
- 章节内表格：`hover:bg-zinc-50` 行悬停效果

### 深色压轴大卡片（最后一章节必用）
```html
<div class="lecture-card fade-up bg-gradient-to-br from-zinc-900 to-zinc-800 text-white border-0">
    <h3 class="text-xl font-semibold mb-6 flex items-center gap-2">
        <span class="text-rose-400">✦</span>
        核心结论 / 关键参数表
    </h3>
</div>
```

### JavaScript 交互
- `scroll-bar` 宽度随滚动百分比变化
- `to-top-btn` 滚动超过 500px 显示
- `.fade-up` 元素 IntersectionObserver 触发后加 `show` 类

---

## 📄 全文总述格式规范（4 板块结构）

### 板块 1：论文概览（Overview）
- 基本信息卡片（主题、作者、年份、会议/期刊、研究方向）
- 核心摘要文字（用 core-idea-text 样式）
- 用对应主题色编号标签

### 板块 2：章节结构（章节列表）
- 表格或卡片列出论文章节标题 + 简短内容摘要

### 板块 3：工作流程 / 研究方法
- 可视化步骤式结构（带序号圆圈 + 连接线）
- 4-6 个步骤描述核心研究/实验/设计流程

### 板块 4：影响与展望
- 核心贡献、学术意义、应用领域
- 深色压轴大卡片总结核心发现 / 参数表 / 未来方向

---

## 🚀 核心功能

### 1. 自动提取 Related Work
- 从 PDF 文件自动识别 Related Work、Background 等章节
- 提取完整的文本内容
- 排除参考文献列表

### 2. 提取引用论文
- 自动识别 [Author Year] 格式的引用
- 去重处理
- 提取作者、年份等信息

### 3. 识别研究主题
- 基于关键词匹配识别研究领域
- 支持的主题：可展曲面、弹性结构、可展开结构、计算设计、制造、网格壳、测地线、折纸、自支撑结构等

### 4. 生成研究脉络报告
- Tailwind CSS 现代风格卡片
- 按主题分类引用论文
- 分析研究演进趋势

### 5. 搜索免费链接 ⭐
- 自动搜索每篇论文的 DOI
- 提供 ACM、IEEE、Springer、Nature 等数据库链接
- 标注核心论文（⭐）

---

## 📖 使用方式

### 方式一：提供 PDF 文件路径（推荐）
```
"帮我分析论文 /path/to/paper.pdf 的 Related Work"
```

### 方式二：提供 Related Work 文本
```
"这是论文的 Related Work 内容，请帮我分析：[内容]"
```

### 方式三：多段文本
```
"我会分段给你 Related Work 内容"
[粘贴第一段]
"继续"
[粘贴第二段]
"结束"
```

---

## 📊 输出内容

### 1. 引用论文列表
| 论文 | 年份 | DOI | 研究方向 |
|------|------|-----|----------|
| Author et al. | 2020 | 10.xxx | 主题 |

### 2. 研究脉络思维导图
```
研究脉络
├─ 主题1
│   ├─ Author [2020]
│   └─ ...
└─ 主题2
```

### 3. 研究方向与创新点
- 总结各论文的核心贡献
- 分析研究演进趋势
- 指出与目标论文的关系

---

## 🔧 技术实现

**依赖工具：**
- `WebFetch` - 网页内容读取
- `pypdf` - PDF 文本提取
- Tailwind CSS CDN - UI 样式
- Google Fonts - Cormorant Garamond + Noto Sans SC

---

## 💡 泛化能力

本 skill 可处理：
- ✅ 任何学术论文（计算机图形学、物理、机械工程等）
- ✅ 任何引用格式（ACM、IEEE、Springer 等）
- ✅ 任何章节命名（Related Work, Background, Prior Work 等）
- ✅ 任何 PDF 格式

---

## 🎯 适用场景

- 📚 论文阅读理解
- 🔬 研究综述写作
- 🎓 学术报告准备
- 💼 技术调研
- 📝 毕业论文 Related Work 章节

---

## ⚠️ 注意事项

1. **PDF 文本提取**：部分 PDF 可能无法提取文本（扫描版）
2. **引用格式**：自动识别 [Author Year] 格式，其他格式需手动处理
3. **免费链接**：尽力搜索，可能部分论文无法找到免费版本
4. **UI 风格**：必须使用 Tailwind CSS 现代风格（见 UI 设计规范）

---

## 🔗 相关资源

- ACM Digital Library: https://dl.acm.org
- IEEE Xplore: https://ieeexplore.ieee.org
- Google Scholar: https://scholar.google.com
- arXiv: https://arxiv.org
- ScienceDirect: https://www.sciencedirect.com
- Tailwind CSS: https://tailwindcss.com
