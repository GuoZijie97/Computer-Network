# Computer-Network
It is a Campus Exchange Website project


Discussion for the 5th week
计算机网络 Group1 工作报告

## 第一部分：系统需求分析

### 一、Feature List用户需求  

本系统是面向清华大学校内师生的闲置物品交易平台。用户通过在网站上注册、登录账号，可以同时作为卖家和买家，发布出售物品信息并检索、购买其他用户发布的物品。
根据用户场景变化和事件流程，系统的Feature List如下：
1. 用户可在网站上注册新账号，并设置登录密码；
2. 用户可通过已注册的账号密码登录进入用户主页，选择进入买家或卖家频道，或查看自己所有的卖出与买入订单信息；
3. 用户可在买家频道浏览所有在售物品，并根据关键词、价格区间等筛选物品列表；
4. 买家可点击查看某一物品的具体描述信息，及其卖家的个人卖家信誉评分和历史订单评价；
5. 买家对想购买的物品点击购买后，系统将提供卖家联系方式，以便买家与卖家进行后续沟通，随后该物品将自动从在售列表中去除；
6. 在完成订单后，买家可在“我的订单”中对购买物品确认已收货，进行留言评价和打分；
7. 用户可在卖家频道发布自己希望出售的物品，并可随时修改和删除待售物品信息；
8. 卖家可在“我的订单”中对卖出物品的买家留言进行查看和回复。


### 二、Use Case Diagram用例图  


### 三、Requirements系统要求  
根据系统Feature List和Use Case分析，我们以Use Case（用例）为驱动因素，得到相应的系统要求如下：
1. 网站需提供新用户注册和用户登录验证功能；
2. 网站为用户提供买家频道、卖家频道和我的订单等模块按钮，点击后可跳转至新的模块页面；
3. 在买家频道中，系统需根据用户选择的筛选条件，选择性地展示相应物品列表；
4. 当买家点击某一物品封面时，网站跳转至物品详细信息页；
5. 在买家点击购买物品后，网站展示卖家联系方式，同时系统在数据库中将该物品从在售物品列表中删除；
6. 在卖家频道中，系统需根据卖家输入的信息向数据库中添加或修改在售物品信息；
7. 系统需根据已售物品的买家评分，定时对每一位卖家计算个人平均信誉得分，展示在卖家信息中。

### 四、Activities Diagram活动图  





## 第二部分：Work Flow Diagram  
### 一、	用户注册  
   用户注册需要同学填写姓名、学号信息等，通过管理员认证方可成功注册。


### 二、	发布商品  
   用户进入后可管理个人商品界面并发布想要出售的商品。同时发布时可设置商品的价格、新旧程度、商品分类等标签。
 

### 三、	购买商品  
   用户进入购买页面后可根据个人需求搜索商品，之后可查看商品详细信息，包括在商品下留言评论获取更多信息。挑选完成后，选择确认购买，便可获得卖家的个人联系方式。考虑到校园交易中当面交易的便利性，学生将通过微信、手机等方式联系彼此并当面交付。交易成功后卖家将在网上确认交易，商品交易信息进入成功订单信息库，同时商品将自动从商品库中撤下。



## 第三部分：系统结构层次分析  
   我们基于对用户需求的分析及网站功能的设计，将项目整体架构划分为应用层、服务层和数据层。在应用层我们主要通过网页与用户对接，用户在网站上进行操作；服务层我们主要实现功能模块的划分、网站与数据库之间的通信及具体业务操作的实现；数据层我们利用MySQL数据库存储用户、商品及交易相关数据，为与网站的交互提供支撑。

### 一、	网络架构设计  
   在网站部分，我们采用树形结构的设计方式，根据工作逻辑和用户使用习惯分为多层级的子栏目，以实现结构清晰、URL语意明确、识别度高、内部链接权值易于传递的目的。
 
网站架构设计图  


### 二、	功能模块划分  
根据系统业务属性进行切分，本网站的功能可以分为五个模块：买家模块、卖家模块、商品模块、订单模块、用户信息模块。  
  
买家模块主要实现购买及咨询功能，同时与商品模块相联系，提供检索筛选的入口。卖家模块主要实现发布及更新商品信息功能，同时可以对留言信息进行操作。订单模块分为历史订单和进行中订单两部分，将买卖双方联系在一起，实现查看订单、确认收货、取消订单及订单评价等功能；商品模块则主要为商品的展示与检索功能提供支撑，提供不同的筛选条件及检索模式，以便用户找到契合的商品，之后用户借助此模块可以查看商品详情、留言评论。用户信息模块则主要实现用户信息的管理，核心是用户名、密码及个人联系方式的管理，功能上为用户验证、分组，线下交易的最终完成提供支撑。
  
以上功能模块的划分与网站的架构设计及数据库表单设计相契合，相互联系且密不可分，对网站完整功能的实现提供逻辑及数据支撑。  

### 三、	数据层  
用户、商品和订单相关信息都将实时存入MySQL数据库中，并根据需求及时更新在网页上。根据功能分析，系统所需要的基本信息列示如下：  
    
1. 用户信息  
用户基本信息在注册时需要用户提供，用户id唯一且后续不可修改，其他信息可改，主要包括：id，昵称，简介，联系方式；同时在商品交易过程中用户作为卖家身份会拥有额外的买家评分信息。

2. 商品信息  
商品信息主要包括商品id、商品名称、图片、分类、简介（品牌、功能，新旧程度等）、价格、其他备注信息、评论与回复信息。

3. 订单信息  
主要包括订单编号、商品id、买家id、卖家id、交易时间、交易评价等信息。

## 第四部分：系统容量分析  
  
在这一节,我们将对二手交易网站的系统容量(吞吐率性能需求)进行分析, 根据电子商务网站主要处理交易事务及高并发的特点,此次估算对象主要包括日 均访问量、每秒并发量及访问峰值。  
由于现在校内还没有正式营运的二手交易网站,我们选取具有相同功能的 “清华搬家季二手交易群”(500 人)进行样本的估算,并根据两者不同的特点 进行参数调整  

### 一、	具体方法  
1. 在毕业季及学期中各随机抽取5天，分别统计发布的出售商品信息数；  
2. 计算均值；  
3. 以47000的总体数来估计总体均值；  
4. 进行参数调整估计最后的搜索、添加商品、订单确认。  

### 二、	具体实施情况  
我们选取了毕业季的5月16号、5月30号、6月4号、6月19号、7月5号进行统计，学期中的9月18号、9月30号、10月8号、10月11号、10月20号进行统计，统计结果如下：

毕业季：
日期	数目	商品名称  
6月16号	35	打印机等  
6月30号	28	零食、奶粉、鞋架等  
7月2号	22	自行车、冲击钻、鞋等  
7月12号	25	插线板、吉他、中性笔、拉杆箱等  
7月18号	24	木制书架、大富翁、显示器、图书等  

学期中：  
日期	数目	商品名称  
9月18号	12	游泳卡等  
9月30号	12	球鞋等  
10月8号	13	衣架等  
10月11号	10	烧壶、中性笔等  
10月20号	19	眼药水、计算器等  

### 三、	数据分析  
1.	根据我们观察，二手交易微信群因为没有商品浏览的功能，交易主要以卖方需求为导向，卖方在群里发布想要出售的二手商品信息后，有需求的买方再与其交涉。我们认为在二手交易网站上，买方与卖方具有相同的获取信息的便利性，所以总需求量将会是微信群的2倍；  
2.	现阶段校内还没有一个较为主流的二手交易平台，同学们进行二手交易的渠道较为分散，而二手交易网站的目标就是将其建设成为一个便利全校同学的主流交易平台，所以，我们估算网站的需求量将是微信群的9-10倍；  
3.	由于二手交易群中仅限有需求的同学发布信息而网站兼具购物、休闲的功能，我们估算网站的访问量将是需求量的4-5倍；  
4.	由于网站现阶段还不支持打折等促销活动，将不会出现天猫、京东双十一这样的T级别的并发量，所以我们对峰值的预估保留在平常量的2-3倍；  
5.	集中访问量：24*0.2 = 4.8小时（二八原则）  
   
### 四、	容量估计  
毕业季：  
1.	微信群日均需求量：47000/500 *（35+28+22+25+24）/5 * 2 = 5038.4  
2.	网站日均需求量：5038.4 * 10 = 50384  
3.	网站日均访问量：50384 * 5 = 251920  
4.	每秒并发量： 251920 /（4.8*60*60） =14.6  
5.	峰值预估：14.6 * 3 = 43.7  
  
学期中：  
1.	微信群日均需求量：47000/500 *（12+12+13+10+19）/5 * 2 = 2481.6  
2.	网站日均需求量：2481.6 * 10 = 24816  
3.	网站日均访问量：24816 * 5 = 124080  
4.	每秒并发量： 124080 /（4.8*60*60） =7.2  
5.	峰值预估：7.2* 3 = 21.5  
  
    根据我们对于并发量及峰值的预估，针对校内学生的二手交易网站的总体容量需求不会很大，即使在毕业季的高峰时段，每秒并发量也不会超过100次。配置服务器方面，以tomcat服务器为例，按一台web服务器支持每秒300个并发计算，我们的二手交易网站仅需要配置一台服务器即可。  


## 第五部分：硬件与软件设计  
这部分是对实际网站的设计，不是原型系统。原型系统将在PC上进行测试  

### 一、	硬件需求分析
   在硬件方面，主要考虑两个问题：服务器的硬件配置与带宽配置。  
  
   服务器的硬件配置主要参考网站的规模及数据处理量。本网站面向的用户群体局限于清华师生，且二手交易并非数据处理密集型业务，一般适用于中小型网站的服务器的处理器及内存即可满足要求。  
  
带宽配置主要取决于用户的并发访问量。  
我们考虑平均带宽需求与峰值期间突发带宽需求。根据对并发访问量的估计，网站运营的大部分时间（学期中），每秒并发访问用户数为7.2（以10计）。在高峰时段（毕业季），每秒并发访问用户数的峰值为43.7（以50计）。  
考虑网站的页面大小，由于网站主页、商品展示页面均需要承载较多的图片，其大小需参考电商网站的网页。我们选择淘宝旗下的二手交易平台“闲鱼”作为参照，闲鱼主页大小约为420KB，单一商品展示页面大小约为200KB。考虑到本网站的页面内容远少于“闲鱼”平台，估计页面大小为“闲鱼”页面大小除以10。假设一个典型用户访问本网站的过程为先访问1次主页、再分别访问3个商品展示页面，则网站的平均网页大小为：   
420 KB /10 * 1/4 + 200 KB /10 * 3/4 = 25.5 KB  
假设带宽利用率为70%，则网站的平均带宽需求为：  
25.5 KB * 10 / 70% = 2.98 Mbps  
网站的峰值带宽需求为：  
25.5 KB * 50 = 10.44 Mbps  
考虑到用户愿意等待网页加载的时长，本网站的带宽需求应比上述结果低一些。  
根据行业内计算带宽需求的经验公式，网站所需带宽/8=高峰同时访问数*平均页面大小，可得本网站峰值带宽需求约为9.96 Mbps，与上述计算吻合。  
  
### 二、	云平台解决方案
相较于传统的硬件解决方案，我们倾向于选择云平台提供的硬件服务。这一决策是由于本网站具有以下几个特性：  
1.	非商业性。本网站旨在服务校内师生，并非商业盈利性网站，需要有效控制成本。使用云服务可有效减少硬件设备方面的固定成本的投入，将其转化为按需付费的可变成本。本网站仅面向清华，用户基数小，且高峰期与非高峰期带宽需求差异大，低固定成本、按使用量计费的方案利于控制整体成本；  
2.	开发管理人员的非专业性。本网站的开发管理团队并非专业的网站开发团队，缺乏硬件管理的经验，云服务供应商可提供成熟的解决方案和可靠的技术支持；  
3.	校园场景的局限性。实体机房的搭建会受到校园面积、学校政策等多方面限制，难度过大。  
  
本项目计划选用腾讯云提供的解决方案，具体包括：实例类型、镜像、云硬盘、网络、云监控、负载均衡、弹性伸缩。  
  
实例类型：  
腾讯云的实例类型由CPU、内存、存储和网络带宽组成不同组合，同一实例类型包括多种实例大小，我们可选定实例类型后确定初始实例大小，未来若业务扩张，可扩展实例大小以满足工作负载。  
本项目选择标准型S3实例，因为此实例提供了平衡的计算、内存和网络资源，符合项目需求。该实例特点包括：  
1.	2.5GHz Intel Xeon® Skylake 6133 处理器，计算性能稳定  
2.	最新一代六通道 DDR4 内存，内存带宽达 2666 MT/s  
3.	更大实例规格，S3.20XLARGE320，提供 80 vCPU 和 320 GB内存（最大实例大小）  
4.	处理器与内存配比为 1:2，1:4  
5.	实例网络性能与规格对应，规格越高网络转发性能强，内网带宽上限越高  
支持全种类云硬盘  
  
项目初始实例可选择S3.LARGE8，参数为4核CPU，8GB内存，内网带宽能力1.5Gbps。  
  
网络：  
使用腾讯云提供的私有网络，根据带宽选择包年包月套餐，本项目选择带宽位于2Mbps至5Mbps之间的套餐，高峰期带宽超出部分按照使用量计费。  
  
负载均衡：  
二手交易业务具有较强的时效性，在毕业季会出现业务量波峰，业务波峰波谷明显，需要弹性调控后端资源。将选用腾讯云提供的专业型场景的负载均衡解决方案。  
 

