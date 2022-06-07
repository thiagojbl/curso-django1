
# from unittest import skip

from django.urls import resolve, reverse
from recipes import views

from .test_recipe_base import RecipeTestBase


# @skip('A mensagem do porquê  eu estou pulando esses testes')
class RecipeCategoryViewTest(RecipeTestBase):

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
