# PerspectiveCoder-LM# PerspectiveCoder-LM# PerspectiveCoder-LM



<div align="center">



[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)<div align="center">This work aims to explore the debating capability of LLMs by proposing the MAD framework, which stands for Multi-Agent System. (TBD)

[![Python](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)

[![OpenAI](https://img.shields.io/badge/OpenAI-GPT--4o-green.svg)](https://openai.com/)



**一个基于多智能体协作的定性编码研究框架**[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)## Brief Introduction



[English](README.md) | 简体中文[![Python](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)TBD



</div>[![OpenAI](https://img.shields.io/badge/OpenAI-GPT--4o-green.svg)](https://openai.com/)



---## Framework



## 📖 项目简介**一个基于多智能体协作的定性编码研究框架**TBD



PerspectiveCoder-LM 是一个创新的定性研究编码系统，利用大语言模型（LLM）构建多智能体协作框架，模拟不同研究视角（positionality）下的编码过程。该系统通过多个AI智能体的协作讨论，生成高质量的定性研究编码本（codebook）。



### 核心特点[English](README_EN.md) | 简体中文# Run



- 🤖 **多智能体协作**: 模拟多个不同背景的研究者进行协作编码## Preparation

- 🎯 **视角驱动**: 基于研究者定位理论（positionality）生成多元视角

- 📊 **结构化编码**: 生成符合定性研究标准的完整编码本</div>

- 🔄 **三阶段流程**: 初始编码 → 评审讨论 → 最终裁决

- 🎨 **可视化界面**: 提供 Streamlit 可视化交互界面  ```shell



------  pip3 install -r requirements.txt



## 🏗️ 系统架构  ```



该系统采用多智能体协作架构，包含六个核心智能体：## 📖 项目简介



```PerspectiveCoder-LM 是一个创新的定性研究编码系统，利用大语言模型（LLM）构建多智能体协作框架，模拟不同研究视角（positionality）下的编码过程。该系统通过多个AI智能体的协作讨论，生成高质量的定性研究编码本（codebook）。

┌─────────────────────────────────────────────────┐

│           Role-Agents (角色智能体)              │### 核心特点

│  ┌─────────┐  ┌─────────┐  ┌─────────┐        │

│  │ Role 1  │  │ Role 2  │  │ Role 3  │        │- 🤖 **多智能体协作**: 模拟多个不同背景的研究者进行协作编码

│  └────┬────┘  └────┬────┘  └────┬────┘        │- 🎯 **视角驱动**: 基于研究者定位理论（positionality）生成多元视角

│       │            │            │               │- 📊 **结构化编码**: 生成符合定性研究标准的完整编码本

│       └────────────┼────────────┘               │- 🔄 **三阶段流程**: 初始编码 → 评审讨论 → 最终裁决

│                    ▼                             │- 🎨 **可视化界面**: 提供 Streamlit 可视化交互界面

│           ┌─────────────────┐                   │

│           │  Reviewer-Agent │                   │---

│           │   (评审智能体)   │                   │

│           └────────┬────────┘                   │## 🏗️ 系统架构

│                    ▼                             │

│           ┌─────────────────┐                   │该系统采用多智能体协作架构，包含六个核心智能体：

│           │ Discussion-Agent│                   │

│           │   (讨论智能体)   │                   │```

│           └────────┬────────┘                   │┌─────────────────────────────────────────────────┐

│                    ▼                             ││           Role-Agents (角色智能体)              │

│           ┌─────────────────┐                   ││  ┌─────────┐  ┌─────────┐  ┌─────────┐        │

│           │   Judge-Agent   │                   ││  │ Role 1  │  │ Role 2  │  │ Role 3  │        │

│           │   (裁决智能体)   │                   ││  └────┬────┘  └────┬────┘  └────┬────┘        │

│           └─────────────────┘                   ││       │            │            │               │

└─────────────────────────────────────────────────┘│       └────────────┼────────────┘               │

```│                    ▼                             │

│           ┌─────────────────┐                   │

### 智能体角色说明│           │  Reviewer-Agent │                   │

│           │   (评审智能体)   │                   │

1. **Role-Agents (角色智能体)**│           └────────┬────────┘                   │

   - 基于不同的研究视角生成初始编码本│                    ▼                             │

   - 每个角色具有独特的定位声明（positionality statement）│           ┌─────────────────┐                   │

   - 执行开放式编码（open coding）│           │ Discussion-Agent│                   │

│           │   (讨论智能体)   │                   │

2. **Reviewer-Agent (评审智能体)**│           └────────┬────────┘                   │

   - 比较所有角色智能体的编码结果│                    ▼                             │

   - 识别编码间的一致性（agreement）和分歧（disagreement）│           ┌─────────────────┐                   │

│           │   Judge-Agent   │                   │

3. **Discussion-Agent (讨论智能体)**│           │   (裁决智能体)   │                   │

   - 对分歧编码进行结构化讨论│           └─────────────────┘                   │

   - 基于证据进行单轮讨论解决分歧└─────────────────────────────────────────────────┘

   - 生成统一的决策编码本```



4. **Judge-Agent (裁决智能体)**### 智能体角色说明

   - 作为最终裁决者做出独立判断

   - 整合所有智能体的输出1. **Role-Agents (角色智能体)**

   - 生成最终权威编码本   - 基于不同的研究视角生成初始编码本

   - 每个角色具有独特的定位声明（positionality statement）

---   - 执行开放式编码（open coding）



## 🚀 快速开始2. **Reviewer-Agent (评审智能体)**

   - 比较所有角色智能体的编码结果

### 环境要求   - 识别编码间的一致性（agreement）和分歧（disagreement）



- Python 3.8+3. **Discussion-Agent (讨论智能体)**

- Conda (推荐)   - 对分歧编码进行结构化讨论

- OpenAI API Key   - 基于证据进行单轮讨论解决分歧

   - 生成统一的决策编码本

### 安装步骤

4. **Judge-Agent (裁决智能体)**

1. **克隆仓库**   - 作为最终裁决者做出独立判断

```bash   - 整合所有智能体的输出

git clone https://github.com/haonanwang628/PerspectiveCoder-LM.git   - 生成最终权威编码本

cd PerspectiveCoder-LM

```---



2. **创建虚拟环境**## 🚀 快速开始

```bash

conda create -n torchenv python=3.8### 环境要求

conda activate torchenv

```- Python 3.8+

- Conda (推荐)

3. **安装依赖**- OpenAI API Key

```bash

pip install -r requirements.txt### 安装步骤

```

1. **克隆仓库**

4. **配置 API 密钥**```bash

git clone https://github.com/haonanwang628/PerspectiveCoder-LM.git

在 `config/model_menu.py` 中配置您的 API 密钥：cd PerspectiveCoder-LM

```python```

api_key = {

    "gpt-4o": "your-api-key-here",2. **创建虚拟环境**

    "gpt-4o-mini": "your-api-key-here"```bash

}conda create -n torchenv python=3.8

```conda activate torchenv

```

### 基本使用

3. **安装依赖**

#### 1. 多智能体讨论模式（推荐）```bash

pip install -r requirements.txt

```bash```

python main.py -i "Data/Scrum-interviews/processed/Scrum.json" -o "Data/Scrum-interviews/gpt-4o_output" -m "gpt-4o" -exp 0 -rq "How Do Scrum Practitioners Define Software Quality?"

```4. **配置 API 密钥**



#### 2. 单智能体基线模式在 `config/model_menu.py` 中配置您的 API 密钥：

```python

```bashapi_key = {

python main.py -i "Data/Scrum-interviews/processed/Scrum.json" -o "Data/Scrum-interviews/gpt-4o_output" -m "gpt-4o" -exp 1    "gpt-4o": "your-api-key-here",

```    "gpt-4o-mini": "your-api-key-here"

}

#### 3. 相同视角多智能体模式```



```bash### 基本使用

python main.py -i "Data/Scrum-interviews/processed/Scrum.json" -o "Data/Scrum-interviews/gpt-4o_output" -m "gpt-4o" -exp 2

```#### 1. 多智能体讨论模式（推荐）



### 参数说明```bash

python main.py -i "Data/Scrum-interviews/processed/Scrum.json" -o "Data/Scrum-interviews/gpt-4o_output" -m "gpt-4o" -exp 0 -rq "How Do Scrum Practitioners Define Software Quality?"

| 参数 | 说明 | 默认值 |```

|------|------|--------|

| `-i, --input-file` | 输入数据文件路径（JSON格式） | - |#### 2. 单智能体基线模式

| `-o, --output-dir` | 输出目录路径 | - |

| `-c, --config-dir` | 配置文件路径 | `config/config.json` |```bash

| `-m, --model-name` | 使用的模型名称 | `gpt-4o` |python main.py -i "Data/Scrum-interviews/processed/Scrum.json" -o "Data/Scrum-interviews/gpt-4o_output" -m "gpt-4o" -exp 1

| `-rq, --research-question` | 研究问题 | - |```

| `-exp, --experiment-name` | 实验模式 (0:讨论, 1:基线1, 2:基线2) | `0` |

#### 3. 相同视角多智能体模式

---

```bash

## 📂 项目结构python main.py -i "Data/Scrum-interviews/processed/Scrum.json" -o "Data/Scrum-interviews/gpt-4o_output" -m "gpt-4o" -exp 2

```

```

PerspectiveCoder-LM/### 参数说明

├── main.py                    # 主程序入口

├── requirements.txt           # 依赖包列表| 参数 | 说明 | 默认值 |

├── README.md                  # 项目说明文档|------|------|--------|

│| `-i, --input-file` | 输入数据文件路径（JSON格式） | - |

├── config/                    # 配置文件目录| `-o, --output-dir` | 输出目录路径 | - |

│   ├── config.json           # 主配置文件（智能体提示模板）| `-c, --config-dir` | 配置文件路径 | `config/config.json` |

│   ├── discuss_config0.json  # 讨论配置| `-m, --model-name` | 使用的模型名称 | `gpt-4o` |

│   ├── discuss_menu.py       # 讨论配置菜单| `-rq, --research-question` | 研究问题 | - |

│   └── model_menu.py         # 模型配置菜单| `-exp, --experiment-name` | 实验模式 (0:讨论, 1:基线1, 2:基线2) | `0` |

│

├── utils/                     # 工具模块---

│   ├── Agent.py              # 基础智能体类

│   ├── Agent_discuss.py      # 讨论流程智能体## 📂 项目结构

│   ├── DataLoader.py         # 数据加载器

│   ├── DataProcess.py        # 数据处理工具```

│   ├── Dataset.py            # 数据集类PerspectiveCoder-LM/

│   └── Function.py           # 通用函数├── main.py                    # 主程序入口

│├── requirements.txt           # 依赖包列表

├── Data/                      # 数据目录├── README.md                  # 项目说明文档

│   └── Scrum-interviews/     # Scrum 访谈数据│

│       ├── orgin/            # 原始数据├── config/                    # 配置文件目录

│       ├── processed/        # 处理后数据│   ├── config.json           # 主配置文件（智能体提示模板）

│       └── gpt-4o_output/    # 模型输出结果│   ├── discuss_config0.json  # 讨论配置

│           ├── baseline1/    # 基线模式1结果│   ├── discuss_menu.py       # 讨论配置菜单

│           ├── discuss_process/  # 讨论模式结果│   └── model_menu.py         # 模型配置菜单

│           └── ...│

│├── utils/                     # 工具模块

├── evaluate/                  # 评估模块│   ├── Agent.py              # 基础智能体类

│   ├── eval-pr.py            # 评估脚本│   ├── Agent_discuss.py      # 讨论流程智能体

│   └── 1/                    # 评估实验│   ├── DataLoader.py         # 数据加载器

│       ├── eval.py│   ├── DataProcess.py        # 数据处理工具

│       ├── SBERT.py          # 句子嵌入评估│   ├── Dataset.py            # 数据集类

│       └── all-MiniLM-L6-v2/ # 预训练模型│   └── Function.py           # 通用函数

││

└── streamlit/                 # 可视化界面├── Data/                      # 数据目录

    ├── pages/                # Streamlit 页面│   └── Scrum-interviews/     # Scrum 访谈数据

    │   ├── LLMs-HumanTeamDiscussion.py│       ├── orgin/            # 原始数据

    │   ├── LLMsTeamDiscussion.py│       ├── processed/        # 处理后数据

    │   ├── SingleLLM-1.py│       └── gpt-4o_output/    # 模型输出结果

    │   ├── SingleLLM-2.py│           ├── baseline1/    # 基线模式1结果

    │   └── vis_codebook.py│           ├── discuss_process/  # 讨论模式结果

    ├── LLMs-HumanOutput/     # 人机协作输出│           └── ...

    └── LLMsTeamOutput/       # 多智能体输出│

```├── evaluate/                  # 评估模块

│   ├── eval-pr.py            # 评估脚本

---│   └── 1/                    # 评估实验

│       ├── eval.py

## 🔬 工作流程│       ├── SBERT.py          # 句子嵌入评估

│       └── all-MiniLM-L6-v2/ # 预训练模型

### 完整编码流程│

└── streamlit/                 # 可视化界面

```mermaid    ├── pages/                # Streamlit 页面

graph TB    │   ├── LLMs-HumanTeamDiscussion.py

    A[输入数据] --> B[生成研究者定位声明]    │   ├── LLMsTeamDiscussion.py

    B --> C[多角色初始编码]    │   ├── SingleLLM-1.py

    C --> D[Reviewer评审分类]    │   ├── SingleLLM-2.py

    D --> E{是否有分歧?}    │   └── vis_codebook.py

    E -->|是| F[Discussion结构化讨论]    ├── LLMs-HumanOutput/     # 人机协作输出

    E -->|否| G[Judge最终裁决]    └── LLMsTeamOutput/       # 多智能体输出

    F --> G```

    G --> H[输出最终编码本]

```---



### 详细步骤## 🔬 工作流程



1. **定位声明生成（Positionality Statement）**### 完整编码流程

   - 基于五个维度生成研究者定位

   - 角色身份、学术水平、学科领域、研究兴趣、偏见假设```mermaid

graph TB

2. **初始编码（Open Coding）**    A[输入数据] --> B[生成研究者定位声明]

   - 每个角色智能体独立进行开放式编码    B --> C[多角色初始编码]

   - 遵循归纳编码流程    C --> D[Reviewer评审分类]

   - 生成结构化编码本    D --> E{是否有分歧?}

    E -->|是| F[Discussion结构化讨论]

3. **评审阶段（Review）**    E -->|否| G[Judge最终裁决]

   - 比较所有角色的编码结果    F --> G

   - 分类为一致编码和分歧编码    G --> H[输出最终编码本]

```

4. **讨论阶段（Discussion）**

   - 对分歧编码进行证据驱动的讨论### 详细步骤

   - 收集文献、内容、逻辑三类证据

   - 做出保留/删除/对齐决策1. **定位声明生成（Positionality Statement）**

   - 基于五个维度生成研究者定位

5. **裁决阶段（Judge）**   - 角色身份、学术水平、学科领域、研究兴趣、偏见假设

   - 最终裁决者独立评估所有证据

   - 生成权威的最终编码本2. **初始编码（Open Coding）**

   - 每个角色智能体独立进行开放式编码

---   - 遵循归纳编码流程

   - 生成结构化编码本

## 📊 编码本结构

3. **评审阶段（Review）**

生成的编码本遵循标准的定性研究编码格式：   - 比较所有角色的编码结果

   - 分类为一致编码和分歧编码

```json

{4. **讨论阶段（Discussion）**

  "codebook": [   - 对分歧编码进行证据驱动的讨论

    {   - 收集文献、内容、逻辑三类证据

      "code": "编码标签",   - 做出保留/删除/对齐决策

      "definition": "编码定义（一句话）",

      "inclusion_criteria": ["包含标准1", "包含标准2"],5. **裁决阶段（Judge）**

      "exclusion_criteria": ["排除标准1", "排除标准2"],   - 最终裁决者独立评估所有证据

      "typical_examples": ["典型示例1", "典型示例2"],   - 生成权威的最终编码本

      "atypical_examples": ["非典型示例1"],

      "participants": ["参与者ID"],---

      "relevance_to_RQ": "与研究问题的相关性",

      "notes": "备注信息"## 📊 编码本结构

    }

  ]生成的编码本遵循标准的定性研究编码格式：

}

``````json

{

---  "codebook": [

    {

## 🎨 可视化界面      "code": "编码标签",

      "definition": "编码定义（一句话）",

项目提供 Streamlit 可视化界面，支持：      "inclusion_criteria": ["包含标准1", "包含标准2"],

      "exclusion_criteria": ["排除标准1", "排除标准2"],

- 📝 实时编码过程可视化      "typical_examples": ["典型示例1", "典型示例2"],

- 👥 多智能体协作展示      "atypical_examples": ["非典型示例1"],

- 📊 编码本对比分析      "participants": ["参与者ID"],

- 🔍 编码结果查询      "relevance_to_RQ": "与研究问题的相关性",

      "notes": "备注信息"

### 启动可视化界面    }

  ]

```bash}

cd streamlit```

streamlit run pages/LLMsTeamDiscussion.py

```---



---## 🎨 可视化界面



## 🧪 实验模式项目提供 Streamlit 可视化界面，支持：



### 模式 0: 多智能体讨论模式（推荐）- 📝 实时编码过程可视化

- 三个不同视角的角色智能体- 👥 多智能体协作展示

- 完整的评审-讨论-裁决流程- 📊 编码本对比分析

- 适用于复杂的定性研究任务- 🔍 编码结果查询



### 模式 1: 单智能体基线### 启动可视化界面

- 单个智能体独立编码

- 无协作讨论过程```bash

- 用于对比实验cd streamlit

streamlit run pages/LLMsTeamDiscussion.py

### 模式 2: 相同视角多智能体```

- 三个相同视角的角色智能体

- 评估视角多样性的影响---

- 用于消融实验

## 🧪 实验模式

---

### 模式 0: 多智能体讨论模式（推荐）

## 📈 评估方法- 三个不同视角的角色智能体

- 完整的评审-讨论-裁决流程

项目提供多种评估方法：- 适用于复杂的定性研究任务



1. **语义相似度评估**### 模式 1: 单智能体基线

   - 使用 Sentence-BERT 计算编码相似度- 单个智能体独立编码

   - 评估编码本质量- 无协作讨论过程

- 用于对比实验

2. **一致性评估**

   - 计算智能体间编码一致性### 模式 2: 相同视角多智能体

   - 分析分歧模式- 三个相同视角的角色智能体

- 评估视角多样性的影响

3. **人工评估**- 用于消融实验

   - 与人工编码结果对比

   - 专家质量评审---



---## 📈 评估方法



## 🛠️ 技术栈项目提供多种评估方法：



- **核心框架**: Python 3.8+1. **语义相似度评估**

- **LLM接口**: OpenAI API (GPT-4o, GPT-4o-mini)   - 使用 Sentence-BERT 计算编码相似度

- **数据处理**: pandas, numpy   - 评估编码本质量

- **可视化**: Streamlit, matplotlib, seaborn

- **NLP工具**: sentence-transformers, tiktoken2. **一致性评估**

- **评估**: scikit-learn, scipy   - 计算智能体间编码一致性

   - 分析分歧模式

---

3. **人工评估**

## 📝 配置文件说明   - 与人工编码结果对比

   - 专家质量评审

### config.json

包含所有智能体的系统提示和用户提示模板，定义了：---

- Positionality 生成提示

- Coder 编码提示## 🛠️ 技术栈

- Reviewer 评审提示

- Discussion 讨论提示- **核心框架**: Python 3.8+

- Judge 裁决提示- **LLM接口**: OpenAI API (GPT-4o, GPT-4o-mini)

- **数据处理**: pandas, numpy

### model_menu.py- **可视化**: Streamlit, matplotlib, seaborn

配置模型相关参数：- **NLP工具**: sentence-transformers, tiktoken

- API密钥- **评估**: scikit-learn, scipy

- 基础URL

- 模型名称映射---



---## 📝 配置文件说明



## 🤝 贡献指南### config.json

包含所有智能体的系统提示和用户提示模板，定义了：

欢迎贡献代码！请遵循以下步骤：- Positionality 生成提示

- Coder 编码提示

1. Fork 本仓库- Reviewer 评审提示

2. 创建特性分支 (`git checkout -b feature/AmazingFeature`)- Discussion 讨论提示

3. 提交更改 (`git commit -m 'Add some AmazingFeature'`)- Judge 裁决提示

4. 推送到分支 (`git push origin feature/AmazingFeature`)

5. 开启 Pull Request### model_menu.py

配置模型相关参数：

---- API密钥

- 基础URL

## 📄 许可证- 模型名称映射



本项目采用 MIT 许可证 - 查看 [LICENSE](LICENSE) 文件了解详情。---



---## 🤝 贡献指南



## 👥 作者欢迎贡献代码！请遵循以下步骤：



- **Haonan Wang** - [@haonanwang628](https://github.com/haonanwang628)1. Fork 本仓库

2. 创建特性分支 (`git checkout -b feature/AmazingFeature`)

---3. 提交更改 (`git commit -m 'Add some AmazingFeature'`)

4. 推送到分支 (`git push origin feature/AmazingFeature`)

## 🙏 致谢5. 开启 Pull Request



- 感谢 OpenAI 提供的 GPT 模型支持---

- 感谢所有贡献者的付出

- 本项目受定性研究方法论和多智能体系统研究启发## 📄 许可证



---本项目采用 MIT 许可证 - 查看 [LICENSE](LICENSE) 文件了解详情。



## 📮 联系方式---



如有问题或建议，请通过以下方式联系：## 👥 作者



- GitHub Issues: [提交问题](https://github.com/haonanwang628/PerspectiveCoder-LM/issues)- **Haonan Wang** - [@haonanwang628](https://github.com/haonanwang628)

- Email: haonanwang628@example.com

---

---

## 🙏 致谢

## 🔗 相关资源

- 感谢 OpenAI 提供的 GPT 模型支持

- [定性研究编码指南](https://www.qualitative-research.net/)- 感谢所有贡献者的付出

- [OpenAI API 文档](https://platform.openai.com/docs/)- 本项目受定性研究方法论和多智能体系统研究启发

- [多智能体系统](https://en.wikipedia.org/wiki/Multi-agent_system)

---

---

## 📮 联系方式

<div align="center">

如有问题或建议，请通过以下方式联系：

**如果这个项目对您有帮助，请给个⭐️支持一下！**

- GitHub Issues: [提交问题](https://github.com/haonanwang628/PerspectiveCoder-LM/issues)

Made with ❤️ by the PerspectiveCoder Team- Email: haonanwang628@example.com



</div>---


## 🔗 相关资源

- [定性研究编码指南](https://www.qualitative-research.net/)
- [OpenAI API 文档](https://platform.openai.com/docs/)
- [多智能体系统](https://en.wikipedia.org/wiki/Multi-agent_system)

---

<div align="center">

**如果这个项目对您有帮助，请给个⭐️支持一下！**

Made with ❤️ by the PerspectiveCoder Team

</div>
