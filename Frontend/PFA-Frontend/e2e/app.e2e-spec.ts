import { PFAFrontendPage } from './app.po';

describe('pfa-frontend App', () => {
  let page: PFAFrontendPage;

  beforeEach(() => {
    page = new PFAFrontendPage();
  });

  it('should display welcome message', () => {
    page.navigateTo();
    expect(page.getParagraphText()).toEqual('Welcome to app!!');
  });
});
