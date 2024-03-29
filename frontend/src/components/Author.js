import React from 'react'
import '../App.css';


const AuthorItem = ({author}) => {
    return (
        <tr>
            <td>
                {author.first_name}
            </td>
            <td>
                {author.last_name}
            </td>
            <td>
                {author.birthday_year}
            </td>
            <td>
                {author.email}
            </td>
        </tr>
    )
}

const AuthorList = ({authors}) => {
    return (
            <table>
                <th>
                    First name
                </th>
                <th>
                    Last Name
                </th>
                <th>
                    Birthday year
                </th>
                <th>
                    email
                </th>
                {authors.map((author) => <AuthorItem author={author} />)}
            </table>

        )
    }

export default AuthorList