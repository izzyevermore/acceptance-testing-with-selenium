from tests.acceptance.page_model.base_page import BasePage
from tests.acceptance.locators.blog_page import BlogPageLocator


class BlogPage(BasePage):
    @property
    def url(self):
        return super(BlogPage, self).url + '/blog'

    @property
    def posts_section(self):
        return self.driver.find_element(* BlogPageLocator.POSTS_SECTION)

    @property
    def posts(self):
        return self.driver.find_elements(*BlogPageLocator.POST)

    @property
    def add_post_link(self):
        return self.driver.find_element(*BlogPageLocator.ADD_POST_LINK)
