from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_nested import routers

from system_settings.views import HeaderView, FooterView, OrganizationMuseumAdminView, OrganizationView
from account.views import MuseumAdminLogOutView, MuseumAdminLogInView, GetMuseumAdmin, \
                        CustomerLogInView, CustomerLogOutView, CustomerRegisterView, CustomerVerifyView, \
                        CustomerForgotPasswordView, CustomerVerifyResetPasswordView, CustomerResetPasswordView, \
                        CustomerGetMe
from shop.views import ProductCategoryModelViewSet, ProductModelViewSet, IndexProductByOrganizationView, IndexProductView, \
                        RecommendedProductByOrganizationView, RecommendedProductView, IndexProductCategoryByOrganizationView, \
                        ProductCategoryByOrganizationView, ProductByOrganizationView, ProductView

router = DefaultRouter()
museum_admin = DefaultRouter()


router.register(r'header', HeaderView, basename='header-view')
router.register(r'footer', FooterView, basename='footer-view')
router.register(r'organizations', OrganizationView, basename='organizations-view')
router.register(r'new-products', IndexProductView, basename='new-products-view')
router.register(r'recommended-products', RecommendedProductView, basename='product-recommended-view')
router.register(r'products', ProductView, basename='products-view')


organizations_router = routers.NestedDefaultRouter(router, r'organizations', lookup='organization')

# Customer urls 

# api/v1/organizations/slug/new-products
organizations_router.register(r'new-products', IndexProductByOrganizationView, basename='index-products')

# api/v1/organizations/slug/recommended-products
organizations_router.register(r'recommended-products', RecommendedProductByOrganizationView, basename='index-recommended-products')

# api/v1/organizations/slug/index-product-categories
organizations_router.register(r'index-product-categories', IndexProductCategoryByOrganizationView, basename='index-product-categories')

# api/v1/organizations/slug/product-categories
organizations_router.register(r'product-categories', ProductCategoryByOrganizationView, basename='product-categories')

# api/v1/organizations/slug/products
organizations_router.register(r'products', ProductByOrganizationView, basename='products')

# Museum Admin urls
# museum-admin/organizations/
museum_admin.register(r'organizations', OrganizationMuseumAdminView, basename='museum-admin-organization')

# museum-admin/organizations/id/product-categories/
admin_organizations_router = routers.NestedDefaultRouter(museum_admin, r'organizations', lookup='organization')
admin_organizations_router.register(r'product-categories', ProductCategoryModelViewSet, basename='museum-admin-product-category')

# museum-admin/organizations/id/product-categories/id/products
product_categories_router = routers.NestedDefaultRouter(admin_organizations_router, r'product-categories', lookup='category')
product_categories_router.register(r'products', ProductModelViewSet, basename='museum-admin-product')





urlpatterns = [
    # Index
    path(r'', include(router.urls)),
    path(r'', include(organizations_router.urls)),
    # Admin for museum administrators
    path(r'museum-admin/', include(museum_admin.urls)),
    path(r'museum-admin/', include(admin_organizations_router.urls)),
    path(r'museum-admin/', include(product_categories_router.urls)),
    path(r'museum-admin/login/', MuseumAdminLogInView.as_view(), name='museum-admin-login'),
    path(r'museum-admin/logout/', MuseumAdminLogOutView.as_view(), name='museum-admin-logout'),
    path(r'museum-admin/me/', GetMuseumAdmin.as_view(), name='museum-admin-me'),

    # Customer
    path(r'customers/logout/', CustomerLogOutView.as_view(), name='customers-logout'),
    path(r'customers/login/', CustomerLogInView.as_view(), name='customers-login'),
    path(r'customers/register/', CustomerRegisterView.as_view(), name='customers-register'),
    path(r'customers/verify/', CustomerVerifyView.as_view(), name='customers-verify'),
    path(r'customers/forgot-password/', CustomerForgotPasswordView.as_view(), name='customers-forgot-password'),
    path(r'customers/verify-reset-password/', CustomerVerifyResetPasswordView.as_view(), name='customers-verify-reset-password'),
    path(r'customers/reset-password/', CustomerResetPasswordView.as_view(), name='customers-reset-password'),
    path(r'customers/me/', CustomerGetMe.as_view(), name='customers-get-me'),

]