/********************************************************************************
** Form generated from reading UI file 'PrepareIso.ui'
**
** Created by: Qt User Interface Compiler version 5.12.9
**
** WARNING! All changes made in this file will be lost when recompiling UI file!
********************************************************************************/

#ifndef PREPAREISO_H
#define PREPAREISO_H

#include <QtCore/QVariant>
#include <QtWidgets/QApplication>
#include <QtWidgets/QDialog>
#include <QtWidgets/QDialogButtonBox>
#include <QtWidgets/QGridLayout>
#include <QtWidgets/QLabel>
#include <QtWidgets/QLineEdit>
#include <QtWidgets/QPushButton>
#include <QtWidgets/QSpacerItem>

QT_BEGIN_NAMESPACE

class Ui_PrepareMacosImage
{
public:
    QGridLayout *gridLayout;
    QPushButton *bOpenInstallerApp;
    QLabel *label_4;
    QLabel *label_2;
    QLabel *label_3;
    QLabel *label_5;
    QLineEdit *leInstallAppLocation;
    QPushButton *bPrepareIso;
    QLabel *label_6;
    QLabel *label;
    QLabel *label_7;
    QDialogButtonBox *buttonBox;
    QSpacerItem *verticalSpacer;

    void setupUi(QDialog *PrepareMacosImage)
    {
        if (PrepareMacosImage->objectName().isEmpty())
            PrepareMacosImage->setObjectName(QString::fromUtf8("PrepareMacosImage"));
        PrepareMacosImage->resize(627, 302);
        gridLayout = new QGridLayout(PrepareMacosImage);
        gridLayout->setObjectName(QString::fromUtf8("gridLayout"));
        bOpenInstallerApp = new QPushButton(PrepareMacosImage);
        bOpenInstallerApp->setObjectName(QString::fromUtf8("bOpenInstallerApp"));

        gridLayout->addWidget(bOpenInstallerApp, 5, 2, 1, 1);

        label_4 = new QLabel(PrepareMacosImage);
        label_4->setObjectName(QString::fromUtf8("label_4"));

        gridLayout->addWidget(label_4, 6, 0, 1, 2);

        label_2 = new QLabel(PrepareMacosImage);
        label_2->setObjectName(QString::fromUtf8("label_2"));
        label_2->setOpenExternalLinks(true);

        gridLayout->addWidget(label_2, 3, 0, 1, 2);

        label_3 = new QLabel(PrepareMacosImage);
        label_3->setObjectName(QString::fromUtf8("label_3"));

        gridLayout->addWidget(label_3, 4, 0, 1, 1);

        label_5 = new QLabel(PrepareMacosImage);
        label_5->setObjectName(QString::fromUtf8("label_5"));
        QFont font;
        font.setPointSize(28);
        font.setBold(true);
        font.setWeight(75);
        label_5->setFont(font);

        gridLayout->addWidget(label_5, 0, 0, 1, 1);

        leInstallAppLocation = new QLineEdit(PrepareMacosImage);
        leInstallAppLocation->setObjectName(QString::fromUtf8("leInstallAppLocation"));

        gridLayout->addWidget(leInstallAppLocation, 5, 0, 1, 2);

        bPrepareIso = new QPushButton(PrepareMacosImage);
        bPrepareIso->setObjectName(QString::fromUtf8("bPrepareIso"));

        gridLayout->addWidget(bPrepareIso, 6, 2, 1, 1);

        label_6 = new QLabel(PrepareMacosImage);
        label_6->setObjectName(QString::fromUtf8("label_6"));
        QFont font1;
        font1.setPointSize(16);
        label_6->setFont(font1);
        label_6->setWordWrap(true);

        gridLayout->addWidget(label_6, 0, 1, 1, 2);

        label = new QLabel(PrepareMacosImage);
        label->setObjectName(QString::fromUtf8("label"));
        label->setOpenExternalLinks(true);

        gridLayout->addWidget(label, 2, 0, 1, 2);

        label_7 = new QLabel(PrepareMacosImage);
        label_7->setObjectName(QString::fromUtf8("label_7"));
        label_7->setWordWrap(true);

        gridLayout->addWidget(label_7, 8, 0, 1, 2);

        buttonBox = new QDialogButtonBox(PrepareMacosImage);
        buttonBox->setObjectName(QString::fromUtf8("buttonBox"));
        buttonBox->setOrientation(Qt::Horizontal);
        buttonBox->setStandardButtons(QDialogButtonBox::Cancel|QDialogButtonBox::Ok);

        gridLayout->addWidget(buttonBox, 7, 1, 1, 2);

        verticalSpacer = new QSpacerItem(20, 40, QSizePolicy::Minimum, QSizePolicy::Expanding);

        gridLayout->addItem(verticalSpacer, 1, 0, 1, 1);


        retranslateUi(PrepareMacosImage);
        QObject::connect(buttonBox, SIGNAL(accepted()), PrepareMacosImage, SLOT(accept()));
        QObject::connect(buttonBox, SIGNAL(rejected()), PrepareMacosImage, SLOT(reject()));

        QMetaObject::connectSlotsByName(PrepareMacosImage);
    } // setupUi

    void retranslateUi(QDialog *PrepareMacosImage)
    {
        PrepareMacosImage->setWindowTitle(QApplication::translate("PrepareMacosImage", "Dialog", nullptr));
        bOpenInstallerApp->setText(QApplication::translate("PrepareMacosImage", "Open", nullptr));
        label_4->setText(QApplication::translate("PrepareMacosImage", "Create and Image packer can use to create a Virtual Machine", nullptr));
        label_2->setText(QApplication::translate("PrepareMacosImage", "Download the latest - 1 version of <a href=\"https://itunes.apple.com/app/os-x-el-capitan/id1147835434?mt=12\">macOS</a>", nullptr));
        label_3->setText(QApplication::translate("PrepareMacosImage", "macOS Install App location", nullptr));
        label_5->setText(QApplication::translate("PrepareMacosImage", "prepare_iso.sh", nullptr));
        bPrepareIso->setText(QApplication::translate("PrepareMacosImage", "prepare_iso", nullptr));
        label_6->setText(QApplication::translate("PrepareMacosImage", "Create a macOS disk image that packer can use as a reference to create a macOS Virtual Machine", nullptr));
        label->setText(QApplication::translate("PrepareMacosImage", "Download the latest version of <a href=\"https://itunes.apple.com/us/app/macos-sierra/id1127487414?mt=12&l=en-us#\">macOS</a>", nullptr));
        label_7->setText(QApplication::translate("PrepareMacosImage", "NOTE:  Currently must be completed on a macOS machine", nullptr));
    } // retranslateUi

};

namespace Ui {
    class PrepareMacosImage: public Ui_PrepareMacosImage {};
} // namespace Ui

QT_END_NAMESPACE

#endif // PREPAREISO_H
