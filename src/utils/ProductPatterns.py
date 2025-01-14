
class ProductPatterns:

    def __init__(self):
        self.product_patterns = []

    def is_product_page(self, url):

        self.product_patterns = [
            "/product/", "/products/", "/item/", "/items/", "/p/", "/catalog/", "/shop/",
            "/store/", "/buy/", "/offer/", "/deals/", "/detail/", "/details/", "/listing/",
            "/sku/", "/pid/", "/sale/", "/cart/", "/checkout/", "/view/", "/browse/", "/merchandise/",
            "/goods/", "/order/", "/new/", "/featured/", "/special/", "/clearance/", "/category/",
            "/subcategory/", "/collections/", "/brand/", "/brand-name/", "/product-category/",
            "/item-category/", "/item-details/", "/product-details/", "/view-item/", "/view-product/",
            "/quick-view/", "/product-view/", "/product-info/", "/info/", "/prod/", "/itm/", "/itm-info/",
            "/product-page/", "/detail-page/", "/product-overview/", "/product-showcase/", "/product-display/",
            "/single-product/", "/product-profile/", "/profile/", "/quick-buy/", "/instant-buy/", "/hot/",
            "/new-arrivals/", "/best-sellers/", "/top-sellers/", "/featured-product/", "/promo/", "/promo-product/",
            "/discount/", "/discounted/", "/bargain/", "/hot-deals/", "/popular/", "/trending/", "/limited-offer/",
            "/exclusive/", "/online-shop/", "/ecommerce/", "/etail/", "/retail/",
            "/buy-now/", "/now-buying/", "/best-buys/", "/hot-items/", "/top-picks/", "/premium/", "/luxury/",
            "/limited-edition/", "/best-deals/", "/shop-now/", "/shop-the-look/", "/just-arrived/", "/flash-sale/",
            "/special-offer/", "/end-of-season/", "/sale-items/", "/sale-products/", "/shop-sale/", "/on-sale/",
            "/limited-stock/", "/lowest-price/", "/exclusive-deals/", "/hot-picks/", "/shop-best-sellers/",
            "/deals-of-the-day/", "/grab-now/", "/last-chance/", "/deal-of-the-day/", "/seasonal-offers/",
            "/flash-deals/", "/shop-deals/", "/hottest-products/", "/limited-stock-items/", "/view-deals/",
            "/instant-grab/", "/order-now/", "/take-it-now/", "/buy-now-deals/", "/exclusive-buy/",
            "/new-arrival-products/",
            "/must-have-products/", "/trending-products/", "/top-trending-items/", "/unmissable-deals/", "/specials/",
            "/hot-deal-products/", "/online-offer/", "/online-special/", "/latest-arrivals/", "/seasonal-deals/",
            "/popular-items/", "/featured-products/", "/shop-luxury/", "/clearance-sale/", "/limited-availability/",
            "/shop-new-arrivals/", "/premium-items/", "/flash-sale-items/", "/exclusive-products/",
            "/sale-products-now/",
            "/quick-purchase/", "/exclusive-promo/", "/unbeatable-price/", "/hot-product/", "/top-collection/",
            "/super-sale/",
            "/one-time-offer/", "/limited-time-offer/", "/hot-item-sale/", "/best-buy-now/", "/best-picks/",
            "/select-items/",
            "/super-deals/", "/luxury-items/", "/bestselling-products/", "/hot-price/", "/big-discount/",
            "/best-buy-products/",
            "/super-promo/", "/quick-sale/", "/premium-offers/", "/new-sale/", "/best-deal-items/",
            "/flash-sale-products/",
            "/promo-sales/", "/deal-picks/", "/super-discount/", "/only-today/", "/deal-hunter/", "/on-discount/",
            "/limited-time-promo/", "/exclusive-sales/", "/exclusive-deals-now/", "/top-picks-now/",
            "/deal-of-the-week/",
            "/offer-of-the-day/", "/must-have-items/", "/on-discount-products/", "/view-best-sellers/",
            "/trending-now/",
            "/seasonal-items/", "/best-buys-now/", "/discounted-products/", "/special-discounts/", "/deal-finder/",
            "/seasonal-sale/", "/super-sale-products/", "/exclusive-offers-now/", "/luxury-products/",
            "/best-sale-items/",
            "/bargain-hunters/", "/exclusive-deal-items/", "/best-of-the-day/", "/popular-products-now/",
            "/top-sellers-now/",
            "/top-picks-products/", "/mega-deals/", "/last-minute-deals/", "/offer-alerts/", "/hottest-deals-now/",
            "/online-promo/", "/big-discounts-now/", "/hottest-sale-items/", "/top-items-now/",
            "/exclusive-offers-now/",
            "/promo-items-now/", "/top-deals-now/", "/flash-deals-now/", "/today-offers/", "/hot-discounts/",
            "/flash-discount-items/", "/deal-alerts/", "/now-buying-deals/", "/bargain-hunting-items/",
            "/super-promo-products/",
            "/limited-offer-deals/", "/super-buy-now/", "/quick-deals-now/", "/shop-promo/", "/new-season-products/",
            "/quick-purchase-items/", "/exclusive-purchase/", "/shop-limited-edition/", "/hot-offers-now/",
            "/shop-now-sale/",
            "/must-have-deals/", "/buy-now-exclusive/", "/online-best-deals/", "/best-now-picks/", "/offer-now/",
            "/quick-buy-products/", "/must-have-sale/", "/exclusive-buy-now/", "/popular-items-now/",
            "/super-discount-products/",
            "/top-sellers-products/", "/hot-buys-now/", "/promo-deals-now/", "/deal-now/", "/big-discount-items/",
            "/buy-now-top-items/", "/flash-sale-now/", "/super-deals-now/", "/flash-buys/", "/must-have-now/",
            "/discount-buy-now/",
            "/exclusive-buys/", "/must-have-products-now/", "/flash-sale-now-items/", "/exclusive-item-offers/",
            "/super-offers-now/", "/must-buy-now/"
        ]

        return any(pattern in url for pattern in self.product_patterns)
