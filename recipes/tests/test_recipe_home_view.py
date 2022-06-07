
# from unittest import skip

from django.urls import resolve, reverse
from recipes import views

from .test_recipe_base import RecipeTestBase


# @skip('A mensagem do porquê  eu estou pulando esses testes')
class RecipeHomeViewTest(RecipeTestBase):
    def test_recipe_home_view_function_is_correct(self):
        view = resolve(reverse('recipes:home'))
        self.assertIs(view.func, views.home)
    # tearDown

    def test_recipe_home_view_returns_status_code_200_ok(self):
        response = self.client.get(reverse('recipes:home'))
        self.assertEqual(response.status_code, 200)

    def test_recipe_home_view_load_correct_template(self):
        response = self.client.get(reverse('recipes:home'))
        self.assertTemplateUsed(response, 'recipes/pages/home.html')

    # @skip('WIP')
    def test_recipe_home_temlate_shows_no_recipes_found_if_no_resciples(self):
        #  apagar receita
        # Recipe.objects.get(pk=1).delete()
        response = self.client.get(reverse('recipes:home'))
        self.assertIn('No recipes found', response.content.decode('utf-8'))

        # Tenho que escrever mais algumas coisas sobre o test
        # self.fail('Para que eu temine de digitá-lo!')

    def test_recipe_home_template_loads_recipes(self):
        # response_recipes = response.context['recipes']
        # verifica o tamanho da lista recipes
        # self.assertEqual(len(response.context['recipes']), 1)
        # Testa de o título está correto
        # self.assertEqual(response_recipes.first().title, 'Recipe Title')
        # Verificando o contexto
        self.make_recipe(preparation_time=5,
                         author_data={
                             'first_name': 'Joãozinho'
                         },
                         category_data={
                             'name': 'Café da manhã'
                         })
        response = self.client.get(reverse('recipes:home'))
        content = response.content.decode('utf-8')
        response_context_recipes = response.context['recipes']

        self.assertIn('Recipe Title', content)
        self.assertIn('5 Minutos', content)
        self.assertIn('5 Porções', content)
        self.assertIn('Joãozinho', content)
        self.assertIn('Café da manhã', content)
        self.assertEqual(len(response_context_recipes), 1)

    def test_recipe_home_template_dont_load_recipes_not_published(self):
        """Test recipe is_published false dont show"""
        self.make_recipe(is_published=False)

        response = self.client.get(reverse('recipes:home'))
        content = response.content.decode('utf-8')

        self.assertIn('No recipes found', content)
