import click


@click.group()
def create(ctx, conection):
    '''Create a new conection api'''
    pass


@click.command()
@click.pass_context
def search_articles(ctx,data_base):
    '''generate a list of articles in the database'''
    pass


@click.command()
@click.pass_context
def stock_and_prices(ctx,data_base, time):
    '''generate a report of stock and prices of the date'''
    pass

allc = create
allse = search_articles
allst = stock_and_prices
