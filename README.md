# PerspectiveCoder-LM# PerspectiveCoder-LM# PerspectiveCoder-LM



<div align="center">



[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)<div align="center">This work aims to explore the debating capability of LLMs by proposing the MAD framework, which stands for Multi-Agent System. (TBD)

[![Python](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)

[![OpenAI](https://img.shields.io/badge/OpenAI-GPT--4o-green.svg)](https://openai.com/)



**A Multi-Agent Collaborative Framework for Qualitative Research Coding**[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)## Brief Introduction



English | [简体中文](README_zh.md)[![Python](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)TBD



</div>[![OpenAI](https://img.shields.io/badge/OpenAI-GPT--4o-green.svg)](https://openai.com/)



---## Framework



## 📖 Project Overview**一个基于多智能体协作的定性编码研究框架**TBD



PerspectiveCoder-LM is an innovative qualitative research coding system that leverages Large Language Models (LLMs) to build a multi-agent collaborative framework, simulating the coding process from different research perspectives (positionality). The system generates high-quality qualitative research codebooks through collaborative discussions among multiple AI agents.



### Key Features[English](README_EN.md) | 简体中文# Run



- 🤖 **Multi-Agent Collaboration**: Simulates multiple researchers with different backgrounds collaborating on coding## Preparation

- 🎯 **Perspective-Driven**: Generates diverse perspectives based on researcher positionality theory

- 📊 **Structured Coding**: Generates complete codebooks following qualitative research standards</div>

- 🔄 **Three-Phase Workflow**: Initial Coding → Review & Discussion → Final Adjudication

- 🎨 **Visualization Interface**: Provides Streamlit-based interactive visualization  ```shell



------  pip3 install -r requirements.txt



## 🏗️ System Architecture  ```



The system adopts a multi-agent collaborative architecture with six core agents:## 📖 项目简介



```PerspectiveCoder-LM 是一个创新的定性研究编码系统，利用大语言模型（LLM）构建多智能体协作框架，模拟不同研究视角（positionality）下的编码过程。该系统通过多个AI智能体的协作讨论，生成高质量的定性研究编码本（codebook）。

┌─────────────────────────────────────────────────┐

│              Role-Agents                        │### 核心特点

│  ┌─────────┐  ┌─────────┐  ┌─────────┐        │

│  │ Role 1  │  │ Role 2  │  │ Role 3  │        │- 🤖 **多智能体协作**: 模拟多个不同背景的研究者进行协作编码

│  └────┬────┘  └────┬────┘  └────┬────┘        │- 🎯 **视角驱动**: 基于研究者定位理论（positionality）生成多元视角

│       │            │            │               │- 📊 **结构化编码**: 生成符合定性研究标准的完整编码本

│       └────────────┼────────────┘               │- 🔄 **三阶段流程**: 初始编码 → 评审讨论 → 最终裁决

│                    ▼                             │- 🎨 **可视化界面**: 提供 Streamlit 可视化交互界面

│           ┌─────────────────┐                   │

│           │  Reviewer-Agent │                   │---

│           └────────┬────────┘                   │

│                    ▼                             │## 🏗️ 系统架构

│           ┌─────────────────┐                   │

│           │ Discussion-Agent│                   │该系统采用多智能体协作架构，包含六个核心智能体：

│           └────────┬────────┘                   │

│                    ▼                             │```

│           ┌─────────────────┐                   │┌─────────────────────────────────────────────────┐

│           │   Judge-Agent   │                   ││           Role-Agents (角色智能体)              │

│           └─────────────────┘                   ││  ┌─────────┐  ┌─────────┐  ┌─────────┐        │

└─────────────────────────────────────────────────┘│  │ Role 1  │  │ Role 2  │  │ Role 3  │        │

```│  └────┬────┘  └────┬────┘  └────┬────┘        │

│       │            │            │               │

### Agent Roles│       └────────────┼────────────┘               │

│                    ▼                             │

1. **Role-Agents**│           ┌─────────────────┐                   │

   - Generate initial codebooks from different research perspectives│           │  Reviewer-Agent │                   │

   - Each role has a unique positionality statement│           │   (评审智能体)   │                   │

   - Perform open coding│           └────────┬────────┘                   │

│                    ▼                             │

2. **Reviewer-Agent**│           ┌─────────────────┐                   │

   - Compare coding results from all role agents│           │ Discussion-Agent│                   │

   - Identify agreements and disagreements between codes│           │   (讨论智能体)   │                   │

│           └────────┬────────┘                   │

3. **Discussion-Agent**│                    ▼                             │

   - Conduct structured discussions on disagreement codes│           ┌─────────────────┐                   │

   - Evidence-based single-round discussion to resolve disagreements│           │   Judge-Agent   │                   │

   - Generate unified decision codebook│           │   (裁决智能体)   │                   │

│           └─────────────────┘                   │

4. **Judge-Agent**└─────────────────────────────────────────────────┘

   - Make independent judgments as final adjudicator```

   - Integrate outputs from all agents

   - Generate final authoritative codebook### 智能体角色说明



---1. **Role-Agents (角色智能体)**

   - 基于不同的研究视角生成初始编码本

## 🚀 Quick Start   - 每个角色具有独特的定位声明（positionality statement）

   - 执行开放式编码（open coding）

### Requirements

2. **Reviewer-Agent (评审智能体)**

- Python 3.8+   - 比较所有角色智能体的编码结果

- Conda (recommended)   - 识别编码间的一致性（agreement）和分歧（disagreement）

- OpenAI API Key

3. **Discussion-Agent (讨论智能体)**

### Installation   - 对分歧编码进行结构化讨论

   - 基于证据进行单轮讨论解决分歧

1. **Clone the repository**   - 生成统一的决策编码本

```bash

git clone https://github.com/haonanwang628/PerspectiveCoder-LM.git4. **Judge-Agent (裁决智能体)**

cd PerspectiveCoder-LM   - 作为最终裁决者做出独立判断

```   - 整合所有智能体的输出

   - 生成最终权威编码本

2. **Create virtual environment**

```bash---

conda create -n torchenv python=3.8

conda activate torchenv## 🚀 快速开始

```

### 环境要求

3. **Install dependencies**

```bash- Python 3.8+

pip install -r requirements.txt- Conda (推荐)

```- OpenAI API Key



4. **Configure API Key**### 安装步骤



Configure your API key in `config/model_menu.py`:1. **克隆仓库**

```python```bash

api_key = {git clone https://github.com/haonanwang628/PerspectiveCoder-LM.git

    "gpt-4o": "your-api-key-here",cd PerspectiveCoder-LM

    "gpt-4o-mini": "your-api-key-here"```

}

```2. **创建虚拟环境**

```bash

### Basic Usageconda create -n torchenv python=3.8

conda activate torchenv

#### 1. Multi-Agent Discussion Mode (Recommended)```



```bash3. **安装依赖**

python main.py -i "Data/Scrum-interviews/processed/Scrum.json" -o "Data/Scrum-interviews/gpt-4o_output" -m "gpt-4o" -exp 0 -rq "How Do Scrum Practitioners Define Software Quality?"```bash

```pip install -r requirements.txt

```

#### 2. Single-Agent Baseline Mode

4. **配置 API 密钥**

```bash

python main.py -i "Data/Scrum-interviews/processed/Scrum.json" -o "Data/Scrum-interviews/gpt-4o_output" -m "gpt-4o" -exp 1在 `config/model_menu.py` 中配置您的 API 密钥：

``````python

api_key = {

#### 3. Same-Perspective Multi-Agent Mode    "gpt-4o": "your-api-key-here",

    "gpt-4o-mini": "your-api-key-here"

```bash}

python main.py -i "Data/Scrum-interviews/processed/Scrum.json" -o "Data/Scrum-interviews/gpt-4o_output" -m "gpt-4o" -exp 2```

```

### 基本使用

### Parameters

#### 1. 多智能体讨论模式（推荐）

| Parameter | Description | Default |

|-----------|-------------|---------|```bash

| `-i, --input-file` | Input data file path (JSON format) | - |python main.py -i "Data/Scrum-interviews/processed/Scrum.json" -o "Data/Scrum-interviews/gpt-4o_output" -m "gpt-4o" -exp 0 -rq "How Do Scrum Practitioners Define Software Quality?"

| `-o, --output-dir` | Output directory path | - |```

| `-c, --config-dir` | Configuration file path | `config/config.json` |

| `-m, --model-name` | Model name to use | `gpt-4o` |#### 2. 单智能体基线模式

| `-rq, --research-question` | Research question | - |

| `-exp, --experiment-name` | Experiment mode (0:discussion, 1:baseline1, 2:baseline2) | `0` |```bash

python main.py -i "Data/Scrum-interviews/processed/Scrum.json" -o "Data/Scrum-interviews/gpt-4o_output" -m "gpt-4o" -exp 1

---```



## 📂 Project Structure#### 3. 相同视角多智能体模式



``````bash

PerspectiveCoder-LM/python main.py -i "Data/Scrum-interviews/processed/Scrum.json" -o "Data/Scrum-interviews/gpt-4o_output" -m "gpt-4o" -exp 2

├── main.py                    # Main entry point```

├── requirements.txt           # Dependencies list

├── README.md                  # Project documentation### 参数说明

│

├── config/                    # Configuration files| 参数 | 说明 | 默认值 |

│   ├── config.json           # Main config (agent prompt templates)|------|------|--------|

│   ├── discuss_config0.json  # Discussion configuration| `-i, --input-file` | 输入数据文件路径（JSON格式） | - |

│   ├── discuss_menu.py       # Discussion config menu| `-o, --output-dir` | 输出目录路径 | - |

│   └── model_menu.py         # Model configuration menu| `-c, --config-dir` | 配置文件路径 | `config/config.json` |

│| `-m, --model-name` | 使用的模型名称 | `gpt-4o` |

├── utils/                     # Utility modules| `-rq, --research-question` | 研究问题 | - |

│   ├── Agent.py              # Base agent class| `-exp, --experiment-name` | 实验模式 (0:讨论, 1:基线1, 2:基线2) | `0` |

│   ├── Agent_discuss.py      # Discussion flow agent

│   ├── DataLoader.py         # Data loader---

│   ├── DataProcess.py        # Data processing tools

│   ├── Dataset.py            # Dataset class## 📂 项目结构

│   └── Function.py           # Utility functions

│```

├── Data/                      # Data directoryPerspectiveCoder-LM/

│   └── Scrum-interviews/     # Scrum interview data├── main.py                    # 主程序入口

│       ├── orgin/            # Original data├── requirements.txt           # 依赖包列表

│       ├── processed/        # Processed data├── README.md                  # 项目说明文档

│       └── gpt-4o_output/    # Model output results│

│           ├── baseline1/    # Baseline mode 1 results├── config/                    # 配置文件目录

│           ├── discuss_process/  # Discussion mode results│   ├── config.json           # 主配置文件（智能体提示模板）

│           └── ...│   ├── discuss_config0.json  # 讨论配置

││   ├── discuss_menu.py       # 讨论配置菜单

├── evaluate/                  # Evaluation module│   └── model_menu.py         # 模型配置菜单

│   ├── eval-pr.py            # Evaluation script│

│   └── 1/                    # Evaluation experiments├── utils/                     # 工具模块

│       ├── eval.py│   ├── Agent.py              # 基础智能体类

│       ├── SBERT.py          # Sentence embedding evaluation│   ├── Agent_discuss.py      # 讨论流程智能体

│       └── all-MiniLM-L6-v2/ # Pre-trained models│   ├── DataLoader.py         # 数据加载器

││   ├── DataProcess.py        # 数据处理工具

└── streamlit/                 # Visualization interface│   ├── Dataset.py            # 数据集类

    ├── pages/                # Streamlit pages│   └── Function.py           # 通用函数

    │   ├── LLMs-HumanTeamDiscussion.py│

    │   ├── LLMsTeamDiscussion.py├── Data/                      # 数据目录

    │   ├── SingleLLM-1.py│   └── Scrum-interviews/     # Scrum 访谈数据

    │   ├── SingleLLM-2.py│       ├── orgin/            # 原始数据

    │   └── vis_codebook.py│       ├── processed/        # 处理后数据

    ├── LLMs-HumanOutput/     # Human-LLM collaboration output│       └── gpt-4o_output/    # 模型输出结果

    └── LLMsTeamOutput/       # Multi-agent output│           ├── baseline1/    # 基线模式1结果

```│           ├── discuss_process/  # 讨论模式结果

│           └── ...

---│

├── evaluate/                  # 评估模块

## 🔬 Workflow│   ├── eval-pr.py            # 评估脚本

│   └── 1/                    # 评估实验

### Complete Coding Workflow│       ├── eval.py

│       ├── SBERT.py          # 句子嵌入评估

```mermaid│       └── all-MiniLM-L6-v2/ # 预训练模型

graph TB│

    A[Input Data] --> B[Generate Positionality Statements]└── streamlit/                 # 可视化界面

    B --> C[Multi-Role Initial Coding]    ├── pages/                # Streamlit 页面

    C --> D[Reviewer Classification]    │   ├── LLMs-HumanTeamDiscussion.py

    D --> E{Disagreements?}    │   ├── LLMsTeamDiscussion.py

    E -->|Yes| F[Discussion Structured Resolution]    │   ├── SingleLLM-1.py

    E -->|No| G[Judge Final Adjudication]    │   ├── SingleLLM-2.py

    F --> G    │   └── vis_codebook.py

    G --> H[Output Final Codebook]    ├── LLMs-HumanOutput/     # 人机协作输出

```    └── LLMsTeamOutput/       # 多智能体输出

```

### Detailed Steps

---

1. **Positionality Statement Generation**

   - Generate researcher positioning based on five dimensions## 🔬 工作流程

   - Role identity, academic level, discipline, research interest, biases/assumptions

### 完整编码流程

2. **Initial Coding (Open Coding)**

   - Each role agent independently performs open coding```mermaid

   - Follow inductive coding processgraph TB

   - Generate structured codebook    A[输入数据] --> B[生成研究者定位声明]

    B --> C[多角色初始编码]

3. **Review Phase**    C --> D[Reviewer评审分类]

   - Compare coding results from all roles    D --> E{是否有分歧?}

   - Classify into agreement and disagreement codes    E -->|是| F[Discussion结构化讨论]

    E -->|否| G[Judge最终裁决]

4. **Discussion Phase**    F --> G

   - Conduct evidence-driven discussion on disagreement codes    G --> H[输出最终编码本]

   - Collect three types of evidence: literature, content, logic```

   - Make retain/remove/align decisions

### 详细步骤

5. **Adjudication Phase**

   - Final adjudicator independently evaluates all evidence1. **定位声明生成（Positionality Statement）**

   - Generate authoritative final codebook   - 基于五个维度生成研究者定位

   - 角色身份、学术水平、学科领域、研究兴趣、偏见假设

---

2. **初始编码（Open Coding）**

## 📊 Codebook Structure   - 每个角色智能体独立进行开放式编码

   - 遵循归纳编码流程

The generated codebook follows standard qualitative research coding format:   - 生成结构化编码本



```json3. **评审阶段（Review）**

{   - 比较所有角色的编码结果

  "codebook": [   - 分类为一致编码和分歧编码

    {

      "code": "Code Label",4. **讨论阶段（Discussion）**

      "definition": "Code definition (one sentence)",   - 对分歧编码进行证据驱动的讨论

      "inclusion_criteria": ["Inclusion criterion 1", "Inclusion criterion 2"],   - 收集文献、内容、逻辑三类证据

      "exclusion_criteria": ["Exclusion criterion 1", "Exclusion criterion 2"],   - 做出保留/删除/对齐决策

      "typical_examples": ["Typical example 1", "Typical example 2"],

      "atypical_examples": ["Atypical example 1"],5. **裁决阶段（Judge）**

      "participants": ["Participant ID"],   - 最终裁决者独立评估所有证据

      "relevance_to_RQ": "Relevance to research question",   - 生成权威的最终编码本

      "notes": "Additional notes"

    }---

  ]

}## 📊 编码本结构

```

生成的编码本遵循标准的定性研究编码格式：

---

```json

## 🎨 Visualization Interface{

  "codebook": [

The project provides a Streamlit visualization interface supporting:    {

      "code": "编码标签",

- 📝 Real-time coding process visualization      "definition": "编码定义（一句话）",

- 👥 Multi-agent collaboration display      "inclusion_criteria": ["包含标准1", "包含标准2"],

- 📊 Codebook comparison analysis      "exclusion_criteria": ["排除标准1", "排除标准2"],

- 🔍 Coding result query      "typical_examples": ["典型示例1", "典型示例2"],

      "atypical_examples": ["非典型示例1"],

### Launch Visualization Interface      "participants": ["参与者ID"],

      "relevance_to_RQ": "与研究问题的相关性",

```bash      "notes": "备注信息"

cd streamlit    }

streamlit run pages/LLMsTeamDiscussion.py  ]

```}

```

---

---

## 🧪 Experiment Modes

## 🎨 可视化界面

### Mode 0: Multi-Agent Discussion Mode (Recommended)

- Three role agents with different perspectives项目提供 Streamlit 可视化界面，支持：

- Complete review-discussion-adjudication workflow

- Suitable for complex qualitative research tasks- 📝 实时编码过程可视化

- 👥 多智能体协作展示

### Mode 1: Single-Agent Baseline- 📊 编码本对比分析

- Single agent independent coding- 🔍 编码结果查询

- No collaborative discussion process

- For comparison experiments### 启动可视化界面



### Mode 2: Same-Perspective Multi-Agent```bash

- Three role agents with the same perspectivecd streamlit

- Evaluate the impact of perspective diversitystreamlit run pages/LLMsTeamDiscussion.py

- For ablation experiments```



------



## 📈 Evaluation Methods## 🧪 实验模式



The project provides multiple evaluation methods:### 模式 0: 多智能体讨论模式（推荐）

- 三个不同视角的角色智能体

1. **Semantic Similarity Evaluation**- 完整的评审-讨论-裁决流程

   - Calculate coding similarity using Sentence-BERT- 适用于复杂的定性研究任务

   - Evaluate codebook quality

### 模式 1: 单智能体基线

2. **Consistency Evaluation**- 单个智能体独立编码

   - Calculate inter-agent coding consistency- 无协作讨论过程

   - Analyze disagreement patterns- 用于对比实验



3. **Human Evaluation**### 模式 2: 相同视角多智能体

   - Compare with human coding results- 三个相同视角的角色智能体

   - Expert quality review- 评估视角多样性的影响

- 用于消融实验

---

---

## 🛠️ Technology Stack

## 📈 评估方法

- **Core Framework**: Python 3.8+

- **LLM Interface**: OpenAI API (GPT-4o, GPT-4o-mini)项目提供多种评估方法：

- **Data Processing**: pandas, numpy

- **Visualization**: Streamlit, matplotlib, seaborn1. **语义相似度评估**

- **NLP Tools**: sentence-transformers, tiktoken   - 使用 Sentence-BERT 计算编码相似度

- **Evaluation**: scikit-learn, scipy   - 评估编码本质量



---2. **一致性评估**

   - 计算智能体间编码一致性

## 📝 Configuration Files   - 分析分歧模式



### config.json3. **人工评估**

Contains all agent system and user prompt templates, defining:   - 与人工编码结果对比

- Positionality generation prompts   - 专家质量评审

- Coder prompts

- Reviewer prompts---

- Discussion prompts

- Judge prompts## 🛠️ 技术栈



### model_menu.py- **核心框架**: Python 3.8+

Configure model-related parameters:- **LLM接口**: OpenAI API (GPT-4o, GPT-4o-mini)

- API keys- **数据处理**: pandas, numpy

- Base URLs- **可视化**: Streamlit, matplotlib, seaborn

- Model name mappings- **NLP工具**: sentence-transformers, tiktoken

- **评估**: scikit-learn, scipy

---

---

## 🤝 Contributing

## 📝 配置文件说明

Contributions are welcome! Please follow these steps:

### config.json

1. Fork this repository包含所有智能体的系统提示和用户提示模板，定义了：

2. Create a feature branch (`git checkout -b feature/AmazingFeature`)- Positionality 生成提示

3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)- Coder 编码提示

4. Push to the branch (`git push origin feature/AmazingFeature`)- Reviewer 评审提示

5. Open a Pull Request- Discussion 讨论提示

- Judge 裁决提示

---

### model_menu.py

## 📄 License配置模型相关参数：

- API密钥

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.- 基础URL

- 模型名称映射

---

---

## 👥 Authors

## 🤝 贡献指南

- **Haonan Wang** - [@haonanwang628](https://github.com/haonanwang628)

欢迎贡献代码！请遵循以下步骤：

---

1. Fork 本仓库

## 🙏 Acknowledgments2. 创建特性分支 (`git checkout -b feature/AmazingFeature`)

3. 提交更改 (`git commit -m 'Add some AmazingFeature'`)

- Thanks to OpenAI for providing GPT model support4. 推送到分支 (`git push origin feature/AmazingFeature`)

- Thanks to all contributors5. 开启 Pull Request

- This project is inspired by qualitative research methodology and multi-agent systems research

---

---

## 📄 许可证

## 📮 Contact

本项目采用 MIT 许可证 - 查看 [LICENSE](LICENSE) 文件了解详情。

For questions or suggestions, please contact:

---

- GitHub Issues: [Submit an issue](https://github.com/haonanwang628/PerspectiveCoder-LM/issues)

- Email: haonanwang628@example.com## 👥 作者



---- **Haonan Wang** - [@haonanwang628](https://github.com/haonanwang628)



## 🔗 Related Resources---



- [Qualitative Research Coding Guide](https://www.qualitative-research.net/)## 🙏 致谢

- [OpenAI API Documentation](https://platform.openai.com/docs/)

- [Multi-Agent Systems](https://en.wikipedia.org/wiki/Multi-agent_system)- 感谢 OpenAI 提供的 GPT 模型支持

- 感谢所有贡献者的付出

---- 本项目受定性研究方法论和多智能体系统研究启发



<div align="center">---



**If this project helps you, please give it a ⭐️!**## 📮 联系方式



Made with ❤️ by the PerspectiveCoder Team如有问题或建议，请通过以下方式联系：



</div>- GitHub Issues: [提交问题](https://github.com/haonanwang628/PerspectiveCoder-LM/issues)

- Email: haonanwang628@example.com

---

## 🔗 相关资源

- [定性研究编码指南](https://www.qualitative-research.net/)
- [OpenAI API 文档](https://platform.openai.com/docs/)
- [多智能体系统](https://en.wikipedia.org/wiki/Multi-agent_system)

---

<div align="center">

**如果这个项目对您有帮助，请给个⭐️支持一下！**

Made with ❤️ by the PerspectiveCoder Team

</div>
