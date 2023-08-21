from read_data.create_data import main as create_data
from data_analyze.analyze_all import main as analyze_all
from data_analyze.analyze_correlation import main as analyze_correlation
from data_analyze.analyze_multi import main as analyze_multi


def main():
    create_data()
    analyze_all()
    analyze_correlation()
    analyze_multi()
    
if __name__ == '__main__':
    main()
