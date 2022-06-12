# Hurtree 词法分析法
**Hurtree词法分析法**是利用不同<u><b>令牌(Token)</b></u><sup><a href="https://baike.baidu.com/item/Token/2615248">[1]</a></sup>之间<b>优先级顺序(Priority Sequence)</b>所带来的特定规律来对代码进行<u>**词法分析(Lexical Analysis)**</u><sup><a href="https://baike.baidu.com/item/%E8%AF%8D%E6%B3%95%E5%88%86%E6%9E%90">[2]</a></sup>， 解析后是呈现的简单的AST结构. <br><br>

# Syntax Information 概念

**Syntax Information**是一个**令牌优先级顺序处理信息表(Token Priority Sequence Processing Table)**，指定的<u>**词法分析器(Lexical Analyzer)**</u><sup><a href="https://baike.baidu.com/item/%E8%AF%8D%E6%B3%95%E5%88%86%E6%9E%90%E5%99%A8">[3]</a></sup>可以根据 Syntax Information 将代码解析为<u>**抽象语法树 (Abstract Syntax Tree)**</u><sup><a href="https://baike.baidu.com/item/%E6%8A%BD%E8%B1%A1%E8%AF%AD%E6%B3%95%E6%A0%91">[4]</a></sup>.<br>
Syntax Information 中每个<u>**标签(Tag)**</u><sup><a href="https://baike.baidu.com/item/tag/97603">[5]</a></sup>，这里意思同令牌，都可以设置各自的**属性(Attribute)**，不同的属性赋予标签不同的功能。使之，当某个令牌被分析时，不同属性划定了如何对其进行分析以解析出正确的语法抽象树。<br>
在**Syntax Information v1.0-pre**中每个标签最多可以有4种不同属性，分别是 **typeToken**, **rangeDirection**, **hideSymbol**, **endSymbol**.<br><br>

# Syntax Information 标签
在Syntax Information中，若**必要标签(Required Label)** 未被设置，会导致程序无法再正常运行下去. 例如，在Tranquillity Beta中会报出`OSError: Lack of resource integrity.`以表示`资源完整性缺失`；**可设标签(Optional label)** 是可选的，即可以为标签添加可设标签来满足特殊的需求. 对于必要标签和可设标签的定义，取决于标签的**typeToken属性**和标签的功能. <br>
**可设值(Settable Value)** 是每个属性必须有的，每个属性最少有一个可设值. 可设值可以为**规则定义**的，也可以为**用户设置**的，取决于不同属性的功能来决定. 

> 当标签的

- ## typeToken: 
    该属性表示所属令牌的类型，该属性为**必要标签**. 该属性有**sentence**和**codeBlock**两个可设值. <br>
    若可设值为sentence，则表示所属令牌在代码中属于在<b>语句(Sentence)</b>中出现的令牌； 若可设值为codeBlock，则表示所属令牌在代码中属于<b>代码块(Code Block)</b>中出现的令牌. 
- ## rangeDirection: 
    该属性表示所属令牌所要包含的<b>解析代码(Processing Code)</b>相对于所属令牌的方向，该属性为**必要标签**. 该属性有**left**, **bothSide**和**right**三个可设值. <br>

    > **解析代码(Processing Code)** 是令牌周围划定的<b>指定范围(Specified Range)</b>内的代码，其在解析时会被替代为一个表示此代码的指定符号. 此代码在解析时也会被解析，此代码被解析完毕后，这串代码往往由Token和低一层的解析代码所代表的指定符号重新表示. 此解析代码是为了<u>代入</u><sup><a href="https://baike.baidu.com/item/%E4%BB%A3%E5%85%A5/19063857">[6]</a></sup>进其所在的高一层的代码.

    若可设值为left时，则表示指定范围为左边部分，有一片解析代码；同理，若可设值为right时，则表示指定范围为右边部分，有一片解析代码；若可设值为bothSide，则表示指定范围为左边部分和右边部分，有两片解析代码. 
- ## hideSymbol:
    该属性表示所属标签的标签名是否在抽象语法树中被隐藏，即是否将该标签的解析结果直接插入上一级分支. 该属性为**可设标签**. 该属性有**True**和**False**两种可设值.<br>
- ## endSymbol:
    该属性表示所属标签在typeToken属性为codeBlock时的