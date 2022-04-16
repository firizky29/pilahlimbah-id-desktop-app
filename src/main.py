"""
    file testing (setiap modul/file ada komentar kaya gini)
"""
#import transaction.productPage as product
#import transaction.orderPage as order
import pageManager as pm


def main():
    """
        test prosedur (setiap fungsi/prosedur harus ada keterangan kaya gini)
    """
    # product.startPage()
    # order.startPage()
    # print("Test")
    windows = pm.pageManager()
    windows.run()

if __name__ == "__main__":
    main()
# harus diakhiri enter
