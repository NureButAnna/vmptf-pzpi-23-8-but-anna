import { body } from 'express-validator';
 
export const commentCreateValidation = [
    body('text')
        .isString()
        .withMessage('Текст має бути рядком')
        .trim()
        .notEmpty()
        .withMessage('Текст коментаря не може бути порожнім')
        .isLength({ min: 1, max: 500 })
        .withMessage('Текст має бути від 1 до 500 символів'),
];
 