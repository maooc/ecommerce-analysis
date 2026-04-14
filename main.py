import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os
import sys

script_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, script_dir)

from src.analyzer import load_sales_data, perform_comprehensive_analysis
from src.visualizer import generate_all_charts

def generate_report(analysis_results, output_file='output/sales_report.txt'):
    os.makedirs('output', exist_ok=True)
    
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write("=" * 60 + "\n")
        f.write("E-commerce Sales Analysis Report\n")
        f.write("=" * 60 + "\n\n")
        
        revenue = analysis_results['revenue_metrics']
        f.write("REVENUE METRICS\n")
        f.write("-" * 40 + "\n")
        f.write(f"Total Revenue: ${revenue['total_revenue']:,.2f}\n")
        f.write(f"Average Order Value: ${revenue['avg_order_value']:,.2f}\n")
        f.write(f"Median Order Value: ${revenue['median_order_value']:,.2f}\n")
        f.write(f"Total Orders: {revenue['total_orders']}\n\n")
        
        f.write("CATEGORY ANALYSIS\n")
        f.write("-" * 40 + "\n")
        cat_data = analysis_results['category_analysis']
        for idx in cat_data.index:
            row = cat_data.loc[idx]
            f.write(f"{idx}:\n")
            f.write(f"  Revenue: ${row['total_revenue']:,.2f}\n")
            f.write(f"  Orders: {int(row['order_count'])}\n\n")
        
        f.write("REGION ANALYSIS\n")
        f.write("-" * 40 + "\n")
        region_data = analysis_results['region_analysis']
        for idx in region_data.index:
            row = region_data.loc[idx]
            f.write(f"{idx}:\n")
            f.write(f"  Revenue: ${row['total_revenue']:,.2f}\n")
            f.write(f"  Orders: {int(row['order_count'])}\n\n")
        
        f.write("TOP 10 PRODUCTS\n")
        f.write("-" * 40 + "\n")
        top_products = analysis_results['top_products']
        for idx, row in top_products.iterrows():
            f.write(f"{idx}: ${row['total_revenue']:,.2f}\n")
        
        f.write("\n\nKEY INSIGHTS\n")
        f.write("-" * 40 + "\n")
        for insight in analysis_results['insights']:
            f.write(f"- {insight['message']}\n")
    
    print(f"Report saved to {output_file}")

def main():
    print("E-commerce Sales Analysis System v1.0")
    print("=" * 40)
    
    os.makedirs('output', exist_ok=True)
    
    df = load_sales_data('data/sales_data.csv')
    print(f"Loaded {len(df)} orders")
    print(f"Date range: {df['date'].min()} to {df['date'].max()}")
    print(f"Categories: {df['product_category'].unique().tolist()}")
    print(f"Regions: {df['region'].unique().tolist()}")
    
    print("\nPerforming analysis...")
    results = perform_comprehensive_analysis(df)
    
    print("\nRevenue Metrics:")
    revenue = results['revenue_metrics']
    print(f"  Total Revenue: ${revenue['total_revenue']:,.2f}")
    print(f"  Average Order: ${revenue['avg_order_value']:,.2f}")
    print(f"  Total Orders: {revenue['total_orders']}")
    
    print("\nCategory Analysis:")
    for idx, row in results['category_analysis'].iterrows():
        print(f"  {idx}: ${row['total_revenue']:,.2f}")
    
    print("\nGenerating charts...")
    generate_all_charts(results)
    
    print("\nGenerating report...")
    generate_report(results)
    
    print("\nAnalysis complete!")
    print("Output files saved to 'output/' directory")

if __name__ == '__main__':
    main()
