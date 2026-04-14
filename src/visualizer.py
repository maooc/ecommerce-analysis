import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def plot_category_revenue(category_data, save_path='output/category_revenue.png'):
    fig, ax = plt.subplots(figsize=(10, 6))
    
    categories = category_data.index.tolist()
    revenues = category_data['total_revenue'].tolist()
    
    colors = plt.cm.Set3(np.linspace(0, 1, len(categories)))
    
    bars = ax.barh(categories, revenues, color=colors, edgecolor='black')
    
    for bar, revenue in zip(bars, revenues):
        ax.text(bar.get_width() + 10, bar.get_y() + bar.get_height()/2, 
                f'${revenue:,.0f}', va='center', fontsize=10)
    
    ax.set_xlabel('Total Revenue ($)', fontsize=12)
    ax.set_ylabel('Category', fontsize=12)
    ax.set_title('Revenue by Product Category', fontsize=14, fontweight='bold')
    ax.grid(True, alpha=0.3, axis='x')
    
    plt.tight_layout()
    plt.savefig(save_path, dpi=150, bbox_inches='tight')
    plt.close()
    print(f"Saved category revenue chart to {save_path}")

def plot_region_comparison(region_data, save_path='output/region_comparison.png'):
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))
    
    regions = region_data.index.tolist()
    revenues = region_data['total_revenue'].tolist()
    order_counts = region_data['order_count'].tolist()
    
    colors = plt.cm.Paired(np.linspace(0, 1, len(regions)))
    
    ax1.bar(regions, revenues, color=colors, edgecolor='black')
    ax1.set_xlabel('Region', fontsize=12)
    ax1.set_ylabel('Total Revenue ($)', fontsize=12)
    ax1.set_title('Revenue by Region', fontsize=14, fontweight='bold')
    ax1.grid(True, alpha=0.3, axis='y')
    plt.setp(ax1.xaxis.get_majorticklabels(), rotation=45, ha='right')
    
    ax2.bar(regions, order_counts, color=colors, edgecolor='black', alpha=0.8)
    ax2.set_xlabel('Region', fontsize=12)
    ax2.set_ylabel('Number of Orders', fontsize=12)
    ax2.set_title('Orders by Region', fontsize=14, fontweight='bold')
    ax2.grid(True, alpha=0.3, axis='y')
    plt.setp(ax2.xaxis.get_majorticklabels(), rotation=45, ha='right')
    
    plt.tight_layout()
    plt.savefig(save_path, dpi=150, bbox_inches='tight')
    plt.close()
    print(f"Saved region comparison to {save_path}")

def plot_daily_trend(daily_data, save_path='output/daily_trend.png'):
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(14, 10))
    
    dates = daily_data.index
    revenues = daily_data['daily_revenue']
    orders = daily_data['order_count']
    
    ax1.plot(dates, revenues, 'b-o', linewidth=2, markersize=6)
    ax1.fill_between(dates, revenues, alpha=0.3)
    ax1.set_xlabel('Date', fontsize=12)
    ax1.set_ylabel('Daily Revenue ($)', fontsize=12)
    ax1.set_title('Daily Revenue Trend', fontsize=14, fontweight='bold')
    ax1.grid(True, alpha=0.3)
    plt.setp(ax1.xaxis.get_majorticklabels(), rotation=45, ha='right')
    
    ax2.bar(dates, orders, color='steelblue', alpha=0.7, edgecolor='navy')
    ax2.set_xlabel('Date', fontsize=12)
    ax2.set_ylabel('Number of Orders', fontsize=12)
    ax2.set_title('Daily Order Count', fontsize=14, fontweight='bold')
    ax2.grid(True, alpha=0.3, axis='y')
    plt.setp(ax2.xaxis.get_majorticklabels(), rotation=45, ha='right')
    
    plt.tight_layout()
    plt.savefig(save_path, dpi=150, bbox_inches='tight')
    plt.close()
    print(f"Saved daily trend to {save_path}")

def plot_category_pie(category_dist, save_path='output/category_pie.png'):
    fig, ax = plt.subplots(figsize=(10, 8))
    
    labels = list(category_dist.keys())
    sizes = list(category_dist.values())
    
    colors = plt.cm.Set3(np.linspace(0, 1, len(labels)))
    
    explode = [0.05] * len(labels)
    
    wedges, texts, autotexts = ax.pie(sizes, explode=explode, labels=labels, colors=colors,
                                       autopct='%1.1f%%', shadow=True, startangle=90,
                                       textprops={'fontsize': 11})
    
    for autotext in autotexts:
        autotext.set_color('white')
        autotext.set_fontweight('bold')
    
    ax.set_title('Category Distribution', fontsize=14, fontweight='bold')
    
    plt.tight_layout()
    plt.savefig(save_path, dpi=150, bbox_inches='tight')
    plt.close()
    print(f"Saved category pie chart to {save_path}")

def plot_top_products(product_data, save_path='output/top_products.png'):
    fig, ax = plt.subplots(figsize=(12, 6))
    
    products = product_data.index.tolist()[:10]
    revenues = product_data['total_revenue'].tolist()[:10]
    
    colors = plt.cm.viridis(np.linspace(0.2, 0.8, len(products)))
    
    bars = ax.barh(products[::-1], revenues[::-1], color=colors[::-1], edgecolor='black')
    
    for bar, revenue in zip(bars, revenues[::-1]):
        ax.text(bar.get_width() + 10, bar.get_y() + bar.get_height()/2, 
                f'${revenue:,.0f}', va='center', fontsize=10)
    
    ax.set_xlabel('Total Revenue ($)', fontsize=12)
    ax.set_ylabel('Product', fontsize=12)
    ax.set_title('Top 10 Products by Revenue', fontsize=14, fontweight='bold')
    ax.grid(True, alpha=0.3, axis='x')
    
    plt.tight_layout()
    plt.savefig(save_path, dpi=150, bbox_inches='tight')
    plt.close()
    print(f"Saved top products chart to {save_path}")

def plot_payment_method(payment_data, save_path='output/payment_method.png'):
    fig, ax = plt.subplots(figsize=(8, 6))
    
    methods = payment_data.index.tolist()
    revenues = payment_data['total_revenue'].tolist()
    
    colors = ['#2ecc71', '#3498db', '#e74c3c']
    
    bars = ax.bar(methods, revenues, color=colors[:len(methods)], edgecolor='black')
    
    for bar, revenue in zip(bars, revenues):
        ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 20, 
                f'${revenue:,.0f}', ha='center', fontsize=11, fontweight='bold')
    
    ax.set_xlabel('Payment Method', fontsize=12)
    ax.set_ylabel('Total Revenue ($)', fontsize=12)
    ax.set_title('Revenue by Payment Method', fontsize=14, fontweight='bold')
    ax.grid(True, alpha=0.3, axis='y')
    
    plt.tight_layout()
    plt.savefig(save_path, dpi=150, bbox_inches='tight')
    plt.close()
    print(f"Saved payment method chart to {save_path}")

def plot_time_patterns(time_patterns, save_path='output/time_patterns.png'):
    fig, ax = plt.subplots(figsize=(10, 6))
    
    days = list(time_patterns.keys())
    values = list(time_patterns.values())
    
    colors = plt.cm.RdYlGn(np.linspace(0.2, 0.8, len(days)))
    
    bars = ax.bar(days, values, color=colors, edgecolor='black')
    
    for bar, value in zip(bars, values):
        ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 5, 
                f'${value:.0f}', ha='center', fontsize=10)
    
    ax.set_xlabel('Day of Week', fontsize=12)
    ax.set_ylabel('Average Order Value ($)', fontsize=12)
    ax.set_title('Average Order Value by Day of Week', fontsize=14, fontweight='bold')
    ax.grid(True, alpha=0.3, axis='y')
    
    plt.tight_layout()
    plt.savefig(save_path, dpi=150, bbox_inches='tight')
    plt.close()
    print(f"Saved time patterns to {save_path}")

def generate_all_charts(analysis_results):
    import os
    os.makedirs('output', exist_ok=True)
    
    plot_category_revenue(analysis_results['category_analysis'])
    plot_region_comparison(analysis_results['region_analysis'])
    plot_daily_trend(analysis_results['daily_trend'])
    plot_category_pie(analysis_results['category_distribution'])
    plot_top_products(analysis_results['top_products'])
    plot_payment_method(analysis_results['payment_analysis'])
    plot_time_patterns(analysis_results['time_patterns'])

if __name__ == '__main__':
    from analyzer import load_sales_data, perform_comprehensive_analysis
    
    df = load_sales_data()
    results = perform_comprehensive_analysis(df)
    generate_all_charts(results)
    print("All charts generated!")
