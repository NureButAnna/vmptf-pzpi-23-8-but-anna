import { body } from 'express-validator';

export const loginValidator = [
    body('email')
        .notEmpty()
        .withMessage("The field can't be empty")
        .isEmail()
        .withMessage('Incorrect email format'),

    body('password')
        .notEmpty()
        .withMessage("The field can't be empty")
        .isLength({ min: 5 })
        .withMessage('Password should have at least 5 characters'),
];

export const registerValidator = [
    body('email')
        .notEmpty()
        .withMessage("The field can't be empty")
        .isEmail()
        .withMessage('Incorrect email format'),

    body('password')
        .notEmpty()
        .withMessage("The field can't be empty")
        .isLength({ min: 5 })
        .withMessage('Password should have at least 5 characters'),

    body('name')
        .notEmpty()
        .withMessage("The field can't be empty")
        .isLength({ min: 2 })
        .withMessage('Name must contain at least 2 characters'),

    body('surname')
        .notEmpty()
        .withMessage("The field can't be empty")
        .isLength({ min: 2 })
        .withMessage('Name must contain at least 2 characters')
];