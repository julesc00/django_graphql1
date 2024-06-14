"""
{
  books {
    id
    title
    description
    createdAt
    updatedAt
  }
}

{
  book(id: 1) {
    id
    title
    description
  }
}

mutation {
  createBook(title: "GraphQL Kicks Ass", description: "Some cool description of this book.") {
    book{
      id
      title
      description
      createdAt
      updatedAt
    }
  }
}

mutation {
  deleteBook(id: 1) {
    message
  }
}

mutation {
  updateBook(id:2, title:"Title changed", description:"Description changed."){
    book{
      id
      title
      description
      createdAt
      updatedAt
    }
  }
}
"""