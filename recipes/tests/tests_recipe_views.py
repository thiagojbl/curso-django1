
# from unittest import skip

from django.urls import resolve, reverse
from recipes import views

from .test_recipe_base import RecipeTestBase


# @skip('A mensagem do porquê  eu estou pulando esses testes')
class RecipeViewTest(RecipeTestBase):
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

    def test_recipe_category_view_function_is_correct(self):
        view = resolve(reverse("recipes:category", kwargs={"category_id": 1}))
        self.assertIs(view.func, views.category)

    def test_recipe_category_view_returns_404__if_no_recipes_found(self):
        response = self.client.get(
            reverse("recipes:category", kwargs={"category_id": 4}))
        self.assertEqual(response.status_code, 404)

    def test_recipe_category_template_loads_recipes(self):
        # Need a recipe for this test
        need_title = 'This is a category test!'
        self.make_recipe(title=need_title)

        response = self.client.get(reverse('recipes:category', args=(1,)))
        content = response.content.decode('utf-8')

        # check if one recipe exists
        self.assertIn(need_title, content)

    def test_recipe_category_template_dont_load_recipes_not_published(self):
        """Test recipe is_published false dont show"""
        recipe = self.make_recipe(is_published=False)

        response = self.client.get(
            reverse('recipes:recipe', kwargs={'id': recipe.category.id})
        )

        self.assertEqual(response.status_code, 404)

    def test_recipe_detail_view_function_is_correct(self):
        view = resolve(reverse("recipes:recipe", kwargs={"id": 1}))
        self.assertIs(view.func, views.recipes)

    def test_recipe_detail_view_returns_404_if_no_recipes_found(self):
        response = self.client.get(
            reverse('recipes:recipe', kwargs={'id': 4})
        )
        self.assertEqual(response.status_code, 404)

    def test_recipe_detail_template_loads_the_correct_recipe(self):
        need_title = 'This is a detail page! - It load one recipe'
        # Need a recipe for this test
        self.make_recipe(title=need_title)

        response = self.client.get(
            reverse('recipes:recipe', kwargs={'id': 1}))
        content = response.content.decode('utf-8')

        # check if one recipe exists
        self.assertIn(need_title, content)

    def test_recipe_detail_template_dont_load_recipe_not_published(self):
        """Test recipe is_published false dont show"""
        recipe = self.make_recipe(is_published=False)

        response = self.client.get(
            reverse('recipes:recipe', kwargs={'id': recipe.id}))

        self.assertEqual(response.status_code, 404)
        pass
