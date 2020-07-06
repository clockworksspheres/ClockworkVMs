/********************************************************************************
** Form generated from reading UI file 'admin_credentials.ui'
**
** Created by: Qt User Interface Compiler version 5.12.9
**
** WARNING! All changes made in this file will be lost when recompiling UI file!
********************************************************************************/

#ifndef ADMIN_CREDENTIALS_H
#define ADMIN_CREDENTIALS_H

#include <QtCore/QVariant>
#include <QtWidgets/QApplication>
#include <QtWidgets/QDialog>
#include <QtWidgets/QGridLayout>
#include <QtWidgets/QLabel>
#include <QtWidgets/QLineEdit>
#include <QtWidgets/QPushButton>
#include <QtWidgets/QSpacerItem>

QT_BEGIN_NAMESPACE

class Ui_AdministratorCredentials
{
public:
    QGridLayout *gridLayout;
    QLabel *label;
    QLabel *label_2;
    QLineEdit *adminName;
    QLabel *label_3;
    QLineEdit *passwordLineEdit;
    QSpacerItem *horizontalSpacer;
    QPushButton *cancelButton;
    QPushButton *authUserButton;

    void setupUi(QDialog *AdministratorCredentials)
    {
        if (AdministratorCredentials->objectName().isEmpty())
            AdministratorCredentials->setObjectName(QString::fromUtf8("AdministratorCredentials"));
        AdministratorCredentials->resize(366, 170);
        gridLayout = new QGridLayout(AdministratorCredentials);
        gridLayout->setObjectName(QString::fromUtf8("gridLayout"));
        label = new QLabel(AdministratorCredentials);
        label->setObjectName(QString::fromUtf8("label"));
        QSizePolicy sizePolicy(QSizePolicy::Preferred, QSizePolicy::Preferred);
        sizePolicy.setHorizontalStretch(0);
        sizePolicy.setVerticalStretch(1);
        sizePolicy.setHeightForWidth(label->sizePolicy().hasHeightForWidth());
        label->setSizePolicy(sizePolicy);
        QFont font;
        font.setPointSize(16);
        label->setFont(font);

        gridLayout->addWidget(label, 0, 0, 1, 4);

        label_2 = new QLabel(AdministratorCredentials);
        label_2->setObjectName(QString::fromUtf8("label_2"));
        QSizePolicy sizePolicy1(QSizePolicy::Preferred, QSizePolicy::MinimumExpanding);
        sizePolicy1.setHorizontalStretch(0);
        sizePolicy1.setVerticalStretch(1);
        sizePolicy1.setHeightForWidth(label_2->sizePolicy().hasHeightForWidth());
        label_2->setSizePolicy(sizePolicy1);
        label_2->setAlignment(Qt::AlignRight|Qt::AlignTrailing|Qt::AlignVCenter);

        gridLayout->addWidget(label_2, 1, 0, 1, 1);

        adminName = new QLineEdit(AdministratorCredentials);
        adminName->setObjectName(QString::fromUtf8("adminName"));
        QSizePolicy sizePolicy2(QSizePolicy::Expanding, QSizePolicy::Fixed);
        sizePolicy2.setHorizontalStretch(0);
        sizePolicy2.setVerticalStretch(0);
        sizePolicy2.setHeightForWidth(adminName->sizePolicy().hasHeightForWidth());
        adminName->setSizePolicy(sizePolicy2);

        gridLayout->addWidget(adminName, 1, 1, 1, 3);

        label_3 = new QLabel(AdministratorCredentials);
        label_3->setObjectName(QString::fromUtf8("label_3"));
        sizePolicy1.setHeightForWidth(label_3->sizePolicy().hasHeightForWidth());
        label_3->setSizePolicy(sizePolicy1);
        label_3->setAlignment(Qt::AlignRight|Qt::AlignTrailing|Qt::AlignVCenter);

        gridLayout->addWidget(label_3, 2, 0, 1, 1);

        passwordLineEdit = new QLineEdit(AdministratorCredentials);
        passwordLineEdit->setObjectName(QString::fromUtf8("passwordLineEdit"));
        sizePolicy2.setHeightForWidth(passwordLineEdit->sizePolicy().hasHeightForWidth());
        passwordLineEdit->setSizePolicy(sizePolicy2);
        passwordLineEdit->setEchoMode(QLineEdit::Password);

        gridLayout->addWidget(passwordLineEdit, 2, 1, 1, 3);

        horizontalSpacer = new QSpacerItem(158, 17, QSizePolicy::Expanding, QSizePolicy::Minimum);

        gridLayout->addItem(horizontalSpacer, 3, 0, 1, 2);

        cancelButton = new QPushButton(AdministratorCredentials);
        cancelButton->setObjectName(QString::fromUtf8("cancelButton"));
        QSizePolicy sizePolicy3(QSizePolicy::Minimum, QSizePolicy::Fixed);
        sizePolicy3.setHorizontalStretch(0);
        sizePolicy3.setVerticalStretch(0);
        sizePolicy3.setHeightForWidth(cancelButton->sizePolicy().hasHeightForWidth());
        cancelButton->setSizePolicy(sizePolicy3);
        cancelButton->setAutoDefault(false);

        gridLayout->addWidget(cancelButton, 3, 2, 1, 1);

        authUserButton = new QPushButton(AdministratorCredentials);
        authUserButton->setObjectName(QString::fromUtf8("authUserButton"));
        QSizePolicy sizePolicy4(QSizePolicy::Minimum, QSizePolicy::MinimumExpanding);
        sizePolicy4.setHorizontalStretch(0);
        sizePolicy4.setVerticalStretch(0);
        sizePolicy4.setHeightForWidth(authUserButton->sizePolicy().hasHeightForWidth());
        authUserButton->setSizePolicy(sizePolicy4);

        gridLayout->addWidget(authUserButton, 3, 3, 1, 1);


        retranslateUi(AdministratorCredentials);

        authUserButton->setDefault(true);


        QMetaObject::connectSlotsByName(AdministratorCredentials);
    } // setupUi

    void retranslateUi(QDialog *AdministratorCredentials)
    {
        AdministratorCredentials->setWindowTitle(QApplication::translate("AdministratorCredentials", "Administrator Credentials Required", nullptr));
        label->setText(QApplication::translate("AdministratorCredentials", "Please enter administrator credentials for: ", nullptr));
        label_2->setText(QApplication::translate("AdministratorCredentials", "Name: ", nullptr));
        label_3->setText(QApplication::translate("AdministratorCredentials", "Password:", nullptr));
        cancelButton->setText(QApplication::translate("AdministratorCredentials", "Cancel", nullptr));
        authUserButton->setText(QApplication::translate("AdministratorCredentials", "Ok", nullptr));
    } // retranslateUi

};

namespace Ui {
    class AdministratorCredentials: public Ui_AdministratorCredentials {};
} // namespace Ui

QT_END_NAMESPACE

#endif // ADMIN_CREDENTIALS_H
