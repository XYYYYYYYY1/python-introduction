import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
import seaborn as sns
from datetime import datetime

# 图形中文显示
zhfont = matplotlib.font_manager.FontProperties(fname="SourceHanSansSC-Bold.otf")

# 辅助函数：统一设置标题、轴标签的字体
def set_zh_font(ax, title=None, xlabel=None, ylabel=None):
    if title:
        ax.set_title(title, fontproperties=zhfont, fontsize=14)
    if xlabel:
        ax.set_xlabel(xlabel, fontproperties=zhfont)
    if ylabel:
        ax.set_ylabel(ylabel, fontproperties=zhfont)

# 全局风格
sns.set_style("whitegrid")
plt.rcParams['figure.figsize'] = (10, 6)

# 加载数据
df = pd.read_csv('UserBehavior.csv',
                 dtype={
                     'user_id': 'int32',
                     'item_id': 'int32',
                     'behavior_type': 'category',
                     'user_geohash': 'category',
                     'item_category': 'int32'
                 })


# 时间列转换
df['time']=pd.to_datetime(df['time'],format='%Y-%m-%d %H', errors='coerce')

df['date']=df['time'].dt.date
df['hour']    = df['time'].dt.hour
df['weekday'] = df['time'].dt.weekday

print("数据形状:",df.shape)
print("前五行数据:",df.head(5))
print("\n列类型\n:",df.dtypes)
print("\n时间范围:", df['time'].min(), "→", df['time'].max())
print("\n缺失值统计:\n", df.isnull().sum())

# 唯一值统计
print("用户数: ",df['user_id'].nunique())
print("商品数：", df['item_id'].nunique())
print("类目数：", df['item_category'].nunique())

# 行为类型分布
beh_dist = df['behavior_type'].value_counts(normalize=True).sort_index() * 100
print("\n行为类型占比（%）：\n", beh_dist.round(2))

# 图1：行为类型分布柱状图
fig, ax = plt.subplots(figsize=(8, 5))
sns.countplot(x='behavior_type', data=df, hue='behavior_type', palette='Set2',
              order=[1,2,3,4], ax=ax, legend=False)
set_zh_font(ax, title="行为类型分布", xlabel="行为类型", ylabel="次数")
ax.set_xticks([0, 1, 2, 3])
ax.set_xticklabels(['点击', '收藏', '加购', '购买'], fontproperties=zhfont)
plt.show()

# 图2：每日行为总量趋势
daily_total=df.groupby('date').size()
fig,ax=plt.subplots(figsize=(12,5))
daily_total.plot(kind='line',marker='o',color='royalblue', ax=ax)
set_zh_font(ax, title="每日总行为量趋势", xlabel="日期", ylabel="行为次数")
plt.xticks(rotation=45)
plt.show()

# 图3：每小时行为热力图
hour_pivot = df.groupby(['hour', 'behavior_type'], observed=False).size().unstack(fill_value=0)
fig, ax = plt.subplots(figsize=(10, 7))
sns.heatmap(hour_pivot, cmap='YlGnBu', annot=True, fmt='d', ax=ax)
set_zh_font(ax, title="每小时各类行为热力图")
plt.show()

# 图4：星期几行为分布（堆叠柱状图）
wd_beh = df.groupby(['weekday', 'behavior_type'], observed=False).size().unstack(fill_value=0)
fig, ax = plt.subplots(figsize=(10, 6))
wd_beh.plot(kind='bar', stacked=True, colormap='viridis', ax=ax)
set_zh_font(ax, title="星期几行为分布（堆叠）", xlabel="星期", ylabel="次数")
ax.set_xticklabels(['周一','周二','周三','周四','周五','周六','周日'],
                   fontproperties=zhfont, rotation=0)
plt.show()

# 整体转化漏斗
funnel = df['behavior_type'].value_counts().sort_index()
funnel.index = funnel.index.astype(int)
pv_count = funnel.loc[1] if 1 in funnel.index else 1.0
funnel_ratio = (funnel / pv_count * 100).round(2)

fig, ax = plt.subplots(figsize=(8, 5))
sns.barplot(x=['点击', '收藏', '加购', '购买'],
            y=funnel.values,
            color='#4c78a8',
            ax=ax)

for i, ratio in enumerate(funnel_ratio):
    ax.text(i, funnel.values[i]/2, f'{ratio}%',
            ha='center', va='center',
            color='white', fontsize=12,
            fontproperties=zhfont)

set_zh_font(ax, title="整体行为转化漏斗",
            xlabel="行为阶段", ylabel="次数")

ax.set_xticks([0, 1, 2, 3])
ax.set_xticklabels(['点击', '收藏', '加购', '购买'],
                   fontproperties=zhfont,
                   rotation=0)

plt.tight_layout()
plt.show()
print("转化率（以点击为基准）：\n", funnel_ratio)

# Top 20 类目点击量
df['behavior_type'] = df['behavior_type'].astype(int)
top_cat_click = df[df['behavior_type'] == 1]['item_category'].value_counts().head(20)
fig, ax = plt.subplots(figsize=(12, 6))
sns.barplot(x=top_cat_click.values, y=top_cat_click.index.astype(str), ax=ax)
set_zh_font(ax, title="Top 20 类目点击量", xlabel="点击次数", ylabel="类目ID")

#图保存为文件
plt.savefig("top20_点击类目.png", dpi=200, bbox_inches='tight')
plt.show()


# user_geohash 有效率（通常很低）
geohash_rate = df['user_geohash'].notna().mean() * 100
print(f"user_geohash 有值比例：{geohash_rate:.2f}%")

