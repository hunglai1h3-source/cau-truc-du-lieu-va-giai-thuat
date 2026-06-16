from routing import demo_routing_shortest_path
from routing import demo_mst_network
from hashing_tools import demo_order_hash_table
from hashing_tools import demo_hashing_general
from hashing_tools import demo_rolling_coupon_search
from promo_optimizer import demo_dp_basics
from promo_optimizer import demo_combo_knapsack_2d
from promo_optimizer import demo_combo_knapsack_1d
def show_menu():
    print("\n========== POLY-SHIP DSA ASSIGNMENT ==========")
    print("1. Demo routing shortest path")
    print("2. Demo MST network")
    print("3. Demo hash table đơn hàng")
    print("4. Demo hashing tổng hợp")
    print("5. Demo rolling hash")
    print("6. Demo DP cơ bản")
    print("7. Demo combo khuyến mãi")
    print("8. Thoát")
def main():
    while True:
        show_menu()
        choice = input("Nhập lựa chọn: ")
        if choice == "1":
            demo_routing_shortest_path()
        elif choice == "2":
            demo_mst_network()
        elif choice == "3":
            demo_order_hash_table()
        elif choice == "4":
            demo_hashing_general()
        elif choice == "5":
            demo_rolling_coupon_search()
        elif choice == "6":
            demo_dp_basics()
        elif choice == "7":
            demo_combo_knapsack_2d()
            demo_combo_knapsack_1d()
        elif choice == "8":
            print("Thoát chương trình.")
            break
        else:
            print("Lựa chọn không hợp lệ, vui lòng nhập lại.")
if __name__ == "__main__":
    main()