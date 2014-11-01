# Restful endpoints for Cheeper

| Method   | Slug                                    | Description                                                                   | Who's allowed                           |
|----------|-----------------------------------------|-------------------------------------------------------------------------------|-----------------------------------------|
| `POST`   | `/auth-token/`                          | Creates and returns an auth. token                                            | With valid login credentials            |
| `DELETE` | `/auth-token/`                          | Invalidates request's auth. token                                             | With valid token                        |
| `GET`    | `/users/`                               | Retrieves the list of all users                                               | Anyone                                  |
| `POST`   | `/users/`                               | Creates a new user                                                            | Anyone                                  |
| `GET`    | `/users/:user-id/`                      | Retrieves details of a specific user                                          | Anyone                                  |
| `PATCH`  | `/users/:user-id/`                      | Updates details of a specific user                                            | With valid token as :user-id            |
| `DELETE` | `/users/:user-id/`                      | Deletes a specific user                                                       | With valid token as :user-id            |
| `GET`    | `/cheeps/`                              | Retrieves the list of all cheeps                                              | Anyone                                  |
| `POST`   | `/cheeps/`                              | Creates a new cheep                                                           | With valid token                        |
| `GET`    | `/cheeps/:cheep-id/`                    | Retrieves details of a specific cheep                                         | Anyone                                  |
| `PATCH`  | `/cheeps/:cheep-id/`                    | Updates details of a specific cheep                                           | With valid token as author of :cheep-id |
| `DELETE` | `/cheeps/:cheep-id/`                    | Deletes a specific cheep                                                      | With valid token as author of :cheep-id |
| `GET`    | `/users/:user-id/cheeps/`               | Retrieve the list of `:user-id`'s cheeps                                      | Anyone                                  |
| `GET`    | `/users/:user-id/following/`            | Retrieves the list of users that `:user-id` is following                      | With valid token                        |
| `POST`   | `/users/:user-id/following/`            | Adds user to the list that `:user-id` is following                            | With valid token as :user-id            |
| `DELETE` | `/users/:user-id/following/:user-id-2/` | Removes `:user-id-2` from the list that `:user-id` is following               | With valid token as :user-id            |
| `GET`    | `/users/:user-id/followers/`            | Retrieves the list of users that follow `:user-id`                            | With valid token                        |
| `GET`    | `/users/:user-id/stream/`               | Retrieves the list of all cheeps from :user-id and the users that they follow | With valid token as :user-id            |
