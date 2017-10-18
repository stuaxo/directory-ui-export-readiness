from django.conf.urls import url
from django.views.generic import TemplateView

import core.views
import article.views

urlpatterns = [
    url(
        r"^robots\.txt$",
        TemplateView.as_view(
            template_name='robots.txt', content_type='text/plain'
        ),
        name='robots'
    ),
    url(
        r"^$",
        core.views.LandingPagelView.as_view(),
        name='landing-page',
    ),
    url(
        r"^market-research/research-your-market$",
        article.views.DoResearchFirstView.as_view(),
        name='article-research-market',
    ),
    url(
        r"^market-research/define-market-potential$",
        article.views.DefineMarketPotentialView.as_view(),
        name='define-market-potential',
    ),
    url(
        r"^market-research/do-field-research$",
        article.views.DoFieldResearchView.as_view(),
        name='do-field-research',
    ),
    url(
        r"^market-research/analyse-the-competition$",
        article.views.AnalyseTheCompetitionView.as_view(),
        name='analyse-the-competition',
    ),
    url(
        r"^market-research/visit-a-trade-show$",
        article.views.VisitTradeShowView.as_view(),
        name='visit-trade-show',
    ),
    url(
        r"^customer-insight/know-your-customers$",
        article.views.KnowYourCustomerView.as_view(),
        name='know-your-customer',
    ),
    url(
        r"^customer-insight/meet-your-customers$",
        article.views.MeetYourCustomerView.as_view(),
        name='meet-your-customer',
    ),
    url(
        r"^customer-insight/manage-language-differences$",
        article.views.ManageLanguageDifferencesView.as_view(),
        name='manage-language-differences',
    ),
    url(
        r"^customer-insight/understand-your-customers-culture$",
        article.views.UnderstandYourCustomersCultureView.as_view(),
        name='understand-your-cutomers-culture',
    ),
    url(
        r"^finance/get-money-to-export$",
        article.views.GetMoneyToExportView.as_view(),
        name='get-money',
    ),
    url(
        r"^finance/choose-the-right-finance$",
        article.views.ChooseTheRightFinanceView.as_view(),
        name='choose-right-finance',
    ),
    url(
        r"^finance/get-export-finance$",
        article.views.GetExportFinanceView.as_view(),
        name='get-export-finance',
    ),
    url(
        r"^finance/raise-money-by-borrowing$",
        article.views.RaiseMoneyByBorrowingView.as_view(),
        name='raise-money-by-borrowing',
    ),
    url(
        r"^finance/borrow-against-assets$",
        article.views.BorrowAgainstAssetsView.as_view(),
        name='borrow-against-assets',
    ),
    url(
        r"^finance/raise-money-with-investment$",
        article.views.RaiseMoneyWithInvestmentView.as_view(),
        name='raise-money-with-investment',
    ),
    url(
        r"^finance/get-finance-support-from-government$",
        article.views.GetGovernmentFinanceSupportView.as_view(),
        name='get-finance-support-from-government',
    ),
    url(
        r"^business-planning/make-an-export-plan$",
        article.views.MakeExportingPlanView.as_view(),
        name='make-an-export-plan',
    ),
    url(
        r"^business-planning/find-a-route-to-market$",
        article.views.FindARouteToMarketView.as_view(),
        name='find-a-route-to-market',
    ),
    url(
        r"^business-planning/use-an-overseas-agent$",
        article.views.UseOverseasAgentView.as_view(),
        name='use-an-overseas-agent',
    ),
    url(
        r"^business-planning/use-a-distributor$",
        article.views.UseDistributorView.as_view(),
        name='use-a-distributor',
    ),
    url(
        r"^business-planning/choosing-an-agent-or-distributor$",
        article.views.ChoosingAgentOrDistributorView.as_view(),
        name='choosing-an-agent-or-distributor',
    ),
    url(
        r"^business-planning/licensing-and-franchising$",
        article.views.LicenceAndFranchisingView.as_view(),
        name='licensing-and-franchising',
    ),
    url(
        r"^business-planning/license-your-product-or-service$",
        article.views.LicenceYourProductOrServiceView.as_view(),
        name='license-your-product-or-service',
    ),
    url(
        r"^business-planning/franchise-your-business$",
        article.views.FranchiseYourBusinessView.as_view(),
        name='franchise-your-business',
    ),
    url(
        r"^business-planning/start-a-joint-venture$",
        article.views.StartJointVentureView.as_view(),
        name='start-a-joint-venture',
    ),
    url(
        r"^business-planning/set-up-an-overseas-operation$",
        article.views.SetupOverseasOperationView.as_view(),
        name='set-up-an-overseas-operation',
    ),
    url(
        r"^getting-paid/consider-how-youll-get-paid$",
        article.views.ConsiderHowPaidView.as_view(),
        name='consider-how-youll-get-paid',
    ),
    url(
        r"^getting-paid/invoice-currency-and-contents$",
        article.views.InvoiceCurrencyAndContentsView.as_view(),
        name='invoice-currency-and-contents',
    ),
    url(
        r"^getting-paid/decide-when-youll-get-paid$",
        article.views.DecideWhenPaidView.as_view(),
        name='decide-when-youll-get-paid',
    ),
    url(
        r"^getting-paid/payment-methods$",
        article.views.PaymentMethodsView.as_view(),
        name='payment-methods',
    ),
    url(
        r"^getting-paid/insure-against-non-payment$",
        article.views.InsureAgainstNonPaymentView.as_view(),
        name='insure-against-non-payment',
    ),
    url(
        r"^operations-and-compliance/plan-the-logistics$",
        article.views.PlanTheLogisticsView.as_view(),
        name='plan-the-logistics',
    ),
    url(
        r"^operations-and-compliance/use-a-freight-forwarder$",
        article.views.UseFreightForwarderView.as_view(),
        name='use-a-freight-forwarder',
    ),
    url(
        r"^operations-and-compliance/use-incoterms-in-contracts$",
        article.views.UseIncotermsInContractsView.as_view(),
        name='use-incoterms-in-contracts',
    ),
    url(
        r"^operations-and-compliance/get-your-export-documents-right$",
        article.views.GetYourExportDocumentsRightView.as_view(),
        name='get-your-export-documents-right',
    ),
    url(
        r"^operations-and-compliance/set-up-a-website$",
        article.views.SetupWesbiteView.as_view(),
        name='set-up-a-website',
    ),
    url(
        r"^operations-and-compliance/match-your-website-to-your-audience$",
        article.views.MatchYourWebsiteToYourAudienceView.as_view(),
        name='match-your-website-to-your-audience',
    ),
    url(
        r"^operations-and-compliance/what-intellectual-property-is$",
        article.views.WhatInterlectualPropertyIsView.as_view(),
        name='what-intellectual-property-is',
    ),
    url(
        r"^operations-and-compliance/types-of-intellectual-property$",
        article.views.TypesOfInterlectualPropertyView.as_view(),
        name='types-of-intellectual-property',
    ),
    url(
        r"^operations-and-compliance/know-what-IP-you-have$",
        article.views.KnowWhatInterlectualPropertyYouHaveView.as_view(),
        name='know-what-IP-you-have',
    ),
    url(
        r"^operations-and-compliance/ip-protection-in-multiple-countries$",
        article.views.InterlectualPropertyProtectionView.as_view(),
        name='ip-protection-in-multiple-countries',
    ),
]
