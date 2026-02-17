"""
Testes automatizados para navegação do site
"""
import pytest
from playwright.sync_api import Page, expect


class TestNavigation:
    """Testes para navegação do site"""

    def test_home_page_loads(self, page_with_base_url: Page, base_url: str):
        """Verifica se a página inicial carrega"""
        page = page_with_base_url
        page.goto(base_url)
        
        expect(page).to_have_title("Design de Interfaces com Figma")

    def _ensure_menu_visible(self, page: Page):
        """Helper to ensure menu is visible (opens drawer if needed)"""
        # Use more specific selector for the header button to avoid ambiguity
        drawer_button = page.locator("label.md-header__button[for='__drawer']")
        if drawer_button.is_visible():
            drawer_button.click()

    def test_curso_menu_exists(self, page_with_base_url: Page, base_url: str):
        """Verifica se o menu 'Aulas' existe"""
        page = page_with_base_url
        page.goto(base_url)
        
        # Open menu if mobile
        self._ensure_menu_visible(page)
        
        # Procura pelo item de menu "Aulas"
        # Usando match flexível
        link = page.get_by_role("link", name="Aulas").first
        expect(link).to_be_visible()

    def test_material_menu_exists(self, page_with_base_url: Page, base_url: str):
        """Verifica se o menu 'Materiais' existe"""
        page = page_with_base_url
        page.goto(base_url)
        
        self._ensure_menu_visible(page)
        
        # Procura pelo item de menu "Materiais"
        link = page.get_by_role("link", name="Materiais", exact=True).first
        expect(link).to_be_visible()

    def test_print_version_link_exists(self, page_with_base_url: Page, base_url: str):
        """Verifica se o link 'Impressão' existe"""
        page = page_with_base_url
        page.goto(base_url)
        
        # Link de impressão geralmente é um ícone no header ou footer
        # Verificamos a presença no DOM, searching for print_page
        print_link = page.locator("a[href*='print_page']")
        expect(print_link.first).to_be_attached()
